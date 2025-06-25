
# FEV-RIPS Validator API

Este servicio permite validar archivos XML de facturación electrónica en salud frente al esquema XSD de la DIAN.

## Endpoints
- POST `/validate` – Sube un archivo XML para validación.

## Instrucciones para despliegue en Render
1. Subir este proyecto a GitHub.
2. Crear un nuevo servicio Web en Render conectado al repositorio.
3. Usar los comandos de build y start indicados en `.render.yaml`.
