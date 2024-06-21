from django.db import transaction
from estate_manager.celery import app
from agreement.models import Payment


@app.task(name="agreement.tasks.process_unsettled_payment")
def process_unsettled_payment(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        agreement = payment.agreement
        with transaction.atomic():
            agreement.amount_paid += payment.amount_paid
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
