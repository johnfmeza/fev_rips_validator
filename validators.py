
import lxml.etree as ET

def validate_xml(xml_str: str, xsd_path: str) -> str:
    try:
        schema = ET.XMLSchema(file=xsd_path)
        doc = ET.fromstring(xml_str.encode('utf-8'))
        schema.assertValid(doc)
        return "✅ XML válido"
    except ET.DocumentInvalid as e:
        return f"❌ XML inválido:\n{e}"
    except Exception as e:
        return f"❌ Error general:\n{e}"
