
from rest_framework.views import Response


class CustomResponse(Response):
    """
    Custom response class to standardize API responses.
    """

    def __init__(self, data=None, status=None, error=None, message="", **kwargs):
        """
        Initialize the custom response class.
        """
        standard_response = {
            "status": "success" if status in range(200, 300) else "error",
            "status_code": status,
            "error": error or [],
            "data": data or {},
            "message": message,
        }

        super().__init__(data=standard_response, status=status, **kwargs)
