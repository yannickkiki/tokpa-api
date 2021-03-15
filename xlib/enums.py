from enum import Enum


class PaymentMethod(Enum):
    mtn = 'MTN Mobile Money'
    moov = 'Moov Money'

    @staticmethod
    def values():
        return [(k.name, k.value) for k in PaymentMethod]
