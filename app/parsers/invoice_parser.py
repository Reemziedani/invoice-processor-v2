from pypdf import PdfReader
from decimal import Decimal
import re


def read_invoice_pdf(file_path):
    # Open the PDF file
    reader = PdfReader(file_path)

    # Collect text from all PDF pages
    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    # Return the complete PDF text
    return text


def extract_invoice_data(text):
    # Search for the required invoice information
    invoice_number = re.search(r"Factuurnummer:\s*(\S+)", text)

    supplier = re.search(
        r"Microsoft Ireland Operations Ltd", text
    )

    order_number = re.search(r"Bestelnummer:\s*(\S+)", text)

    billing_period = re.search(
        r"Factureringsperiode:\s*(\d{2}-\d{2}-\d{4}\s*-\s*\d{2}-\d{2}-\d{4})",
        text
    )

    amount = re.search(r"Kosten:\s*([\d.,]+)", text)

    # Return all extracted information as a dictionary
    return {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "supplier": supplier.group(0) if supplier else None,
        "order_number": order_number.group(1) if order_number else None,
        "billing_period": billing_period.group(1) if billing_period else None,
        "amount": Decimal(amount.group(1).replace(",", ".")) if amount else None
    }
