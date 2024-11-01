import logging

from third_party.payment.payment_abc import PaymentGateway

logger = logging.getLogger(__name__)


class StripePaymentGateway(PaymentGateway):
    def process_payment(self, amount: float, currency: str) -> bool:
        logger.info(f"Processing ${amount} payment in {currency} via Stripe")
        return True
