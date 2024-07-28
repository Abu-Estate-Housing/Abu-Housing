from datetime import timedelta
import datetime
import os
from slack import WebClient
from django.db import transaction
from dotenv import load_dotenv
from estate_manager.celery import app
from agreement.models import Agreement, Payment

load_dotenv()
client = WebClient(token=os.getenv("SLACK_API_TOKEN"))


@app.task(name="agreement.tasks.process_unsettled_payment")
def process_unsettled_payment(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        agreement = payment.agreement
        with transaction.atomic():
            if agreement.status == Agreement.COMPLETED:
                return
            agreement.amount_paid += payment.amount_paid
            if agreement.price == agreement.amount_paid:
                agreement.status = Agreement.COMPLETED
            agreement.save()
            payment.settled = True
            payment.save()
    except Payment.DoesNotExist:
        # Handle the case where the payment does not exist
        pass


@app.task(name="agreement.tasks.poll_unsettled_payment")
def poll_unsettled_payment():
    payments = Payment.objects.filter(settled=False)
    for payment in payments:
        process_unsettled_payment.delay(payment.id)


@app.task(name="agreement.tasks.send_reminder")
def send_reminder(agreement_id):
    agreement = Agreement.objects.get(id=agreement_id)
    user = f"{agreement.tenant.first_name} {agreement.tenant.last_name}"
    end_date = agreement.end_date
    month = end_date.strftime("%B")
    day = end_date.day
    start_date = agreement.start_date.strftime("%Y")
    balance = agreement.price - agreement.amount_paid
    message = (
        f"Hello, {user} your rent agreement of year {start_date}/{end_date.year} is going to expire on {day} {month} {end_date.year}.\n"
        f"Your current balance for your current agreement is {balance}.\n"
        f"The price for the new agreement will be {agreement.property_name.price}.\n"
        "Please take the necessary steps to renew your agreement.\n"
        "If you have any questions, feel free to contact our support team."
    )

    try:
        slack_channel = os.getenv("SLACK_API_CHANNEL", "")
        print(f"Printing slack channel{slack_channel}")
        client.chat_postMessage(
            channel=slack_channel,
            text=message
        )
        agreement.reminder_sent = True
        agreement.save()
    except Exception as e:
        print("Encountered error sending slack message", e)


@app.task(name="agreement.tasks.poll_agreement")
def poll_agreement():
    now = datetime.datetime.now()
    one_month_from_now = now + timedelta(days=30)
    agreements = Agreement.objects.filter(
        end_date__lte=one_month_from_now).filter(
            reminder_sent=False)
    for agreement in agreements:
        send_reminder.delay(agreement.id)


@app.task(name="agreement.tasks.uncheck_reminder_sent")
def uncheck_reminder_sent():
    today = datetime.datetime.now().date()  # Use .date() to compare just the date part
    near_end_dates = [today + timedelta(days=x) for x in [7, 14]]

    # Directly filter agreements whose end dates are either 7 or 14 days away and reminder_sent is True
    agreements_to_uncheck = Agreement.objects.filter(
        reminder_sent=True,
        end_date__date__in=near_end_dates
    )

    for agreement in agreements_to_uncheck:
        print(f'Near end dates {near_end_dates}')
        print(f'End date of agreement {agreement.end_date}')
        agreement.reminder_sent = False
        agreement.save()
