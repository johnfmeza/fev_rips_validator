
from fastapi import FastAPI, UploadFile, File
from validators import validate_xml

app = FastAPI(title="FEV‑RIPS Validator API")

@app.post("/validate")
async def validar_xml(file: UploadFile = File(...)):
    content = await file.read()
    xml_str = content.decode('utf-8', errors='ignore')
    resultado = validate_xml(xml_str, "schemas/FacturaElectronicaDIAN.xsd")
    return {"result": resultado}
