from injector import Module, provider, singleton

from third_party.payment.payment_abc import PaymentGateway
from third_party.payment.stripe import StripePaymentGateway


class PaymentModule(Module):
    @singleton
    @provider
    def provide_payment_gateway(self) -> PaymentGateway:
        return StripePaymentGateway()
