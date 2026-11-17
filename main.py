import app.parsers.invoice_parser
from app.invoice_service import (
    validate_invoice,
    prepare_invoice_for_database
)


# Read the invoice PDF
invoice_text = app.parsers.invoice_parser.read_invoice_pdf("sample_invoice.pdf")

# Extract all invoice information
invoice_data= app.parsers.invoice_parser.extract_invoice_data(invoice_text)

# Validate the invoice
is_valid = validate_invoice(invoice_data)

# Prepare valid invoice data for database storage
if is_valid:
    prepared_invoice = prepare_invoice_for_database(invoice_data)

    print("Prepared invoice:", prepared_invoice)
else:
    print("Invalid invoice")