import json
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()

with open("data-model.json", "r") as file:
    data_model = json.load(file)

def extract_attribute_names(attributes):
    attribute_names = set()
    for attribute in attributes:
        attribute_names.add(attribute["name"])
        if "attributes" in attribute:
            nested_attributes = extract_attribute_names(attribute["attributes"])
            attribute_names.update(nested_attributes)
    return attribute_names

attribute_names = extract_attribute_names(data_model["attributes"])

class Invoice(BaseModel):
    data: Dict[str, Any]


@app.post("/validate")
async def validate_invoice(invoice: Invoice):
    invalid_attributes = []
    for attribute in invoice.data:
        if attribute not in attribute_names:
            invalid_attributes.append(attribute)
    if invalid_attributes:
        raise HTTPException(status_code=400, detail=f"Invalid attributes: {invalid_attributes}")
    return {"message": "Invoice is valid"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)