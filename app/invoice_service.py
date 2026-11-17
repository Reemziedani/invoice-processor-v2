from decimal import Decimal
from datetime import datetime


def validate_invoice(invoice_data):
    # Check that the invoice number is a non-empty string
    invoice_number = invoice_data.get("invoice_number")

    if not isinstance(invoice_number, str) or not invoice_number.strip():
        return False

    # Check that the supplier is a non-empty string
    supplier = invoice_data.get("supplier")

    if not isinstance(supplier, str) or not supplier.strip():
        return False

    # Check that the amount is a Decimal value
    amount = invoice_data.get("amount")

    if not isinstance(amount, Decimal):
        return False

    # Reject invalid or negative amounts
    if not amount.is_finite() or amount < 0:
        return False

    # All required information is valid
    return True
def prepare_invoice_for_database(invoice_data):
    # Validate the invoice before preparing it
    if not validate_invoice(invoice_data):
        raise ValueError("Invalid invoice data")

    # Get the billing period from the invoice
    billing_period = invoice_data.get("billing_period")

    period_start = None
    period_end = None

    # Convert the billing period into two dates
    if billing_period:
        start_text, end_text = billing_period.split(" - ")

        period_start = datetime.strptime(
            start_text.strip(), "%d-%m-%Y"
        ).date()

        period_end = datetime.strptime(
            end_text.strip(), "%d-%m-%Y"
        ).date()

    # Return the invoice data ready for database storage
    return {
        "invoice_number": invoice_data["invoice_number"],
        "supplier": invoice_data["supplier"],
        "order_number": invoice_data.get("order_number"),
        "period_start": period_start,
        "period_end": period_end,
        "amount_excl_vat": invoice_data["amount"]
    }