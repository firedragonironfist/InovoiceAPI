# InovoiceAPI

Please use the below command in terminal to run the code after installing all the packages mentioned in requirements.txt file

uvicorn main:app --reload

Example request Body to test the API:
{
  "data": {
    "InvoiceNumber": "6642141254",
    "InvoiceDate": "January 11, 2025",
    "ProviderName": "AMERICAN HOME SHIELD",
    "ProviderAddress": "PO Box 222222, Dallas, TX 75234-1234",
    "CustomerName": "MOHAMMAD YOUSUF",
    "CustomerAddress": "2082 Cabrillo Ave, Santa Clara, CA 95230-36321",
    "LineItems": [],
    "Subtotal": null,
    "TotalAmount": "$20.16",
    "PaymentTerms": "Upon Receipt"
  }
}
