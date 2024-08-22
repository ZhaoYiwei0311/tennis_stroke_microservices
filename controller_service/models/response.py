SUCCESS_CODE = '200'


def success(message):
    return Response(message, SUCCESS_CODE)


def failure(errors: dict):
    return Response(errors['message'], errors['code'])


class Response:

    def __init__(self, message, code: str):
        self.message = message
        self.code = code

    def to_dict(self):
        """Serialize the model instance to a dictionary."""
        return {
            'message': self.message,
            'code': self.code
        }

    def __str__(self):
        return f'message = [{self.message}] \n' \
               f'code = {self.code}'