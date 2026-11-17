from decimal import Decimal
from app.invoice_service import validate_invoice


def test_valid_invoice():
    # Prepare an invoice with valid information
    invoice_data = {
        "invoice_number": "INV001",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": Decimal("141.12")
    }

    # Check that the invoice is valid
    assert validate_invoice(invoice_data) is True


def test_missing_invoice_number():
    # Prepare an invoice without an invoice number
    invoice_data = {
        "invoice_number": None,
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": Decimal("141.12")
    }

    # Check that the invoice is invalid
    assert validate_invoice(invoice_data) is False

def test_negative_amount():
    # Prepare an invoice with a negative amount
    invoice_data = {
        "invoice_number": "INV002",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": Decimal("-50.00")
    }

    # Check that a negative amount is rejected
    assert validate_invoice(invoice_data) is False


def test_missing_amount():
    # Prepare an invoice without an amount
    invoice_data = {
        "invoice_number": "INV003",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": None
    }

    # Check that a missing amount is rejected
    assert validate_invoice(invoice_data) is False

def test_invoice_number_only_spaces():
    # Prepare an invoice with an empty-looking number
    invoice_data = {
        "invoice_number": "   ",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": Decimal("141.12")
    }

    # Reject an invoice number containing only spaces
    assert validate_invoice(invoice_data) is False


def test_invalid_amount_type():
    # Prepare an invoice with an amount stored as text
    invoice_data = {
        "invoice_number": "INV004",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": "hello"
    }

    # Reject an amount that is not Decimal
    assert validate_invoice(invoice_data) is False


def test_zero_amount():
    # Prepare an invoice with a zero amount
    invoice_data = {
        "invoice_number": "INV005",
        "supplier": "Microsoft Ireland Operations Ltd",
        "amount": Decimal("0.00")
    }

    # Accept a valid invoice with a zero amount
    assert validate_invoice(invoice_data) is True