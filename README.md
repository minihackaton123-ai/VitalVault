# VitalVault

An interoperable digital health locker with emergency QR triage and multilingual AI prescription summarization.

Built for the **Resurrect 2026** idea round (VCET Puttur). Team: **DeepNova**.

## Problem
- In emergencies, responders cannot quickly see blood group, allergies, chronic conditions and current medicines.
- Health records are scattered across paper files, phone photos and separate hospital portals.
- Prescriptions use medical shorthand, mostly in English, which many patients struggle to understand.

## Planned features
- **Health locker:** upload and store records in one place (FHIR-style JSON format).
- **Emergency QR:** read-only page showing only critical info. Links expire and every access is logged.
- **AI prescription summary:** OCR on a prescription photo, then a plain-language summary in English, Hindi or Kannada. The original is always shown beside the summary.
- **Consent-first sharing:** the patient controls what is shared and can revoke access.

## Tech stack (planned)
- Frontend: React (mobile-friendly web app)
- Backend: Python (FastAPI)
- Database: PostgreSQL + encrypted file storage
- AI: Tesseract OCR + LLM API for summary and translation

## What is in this repo now
| File | What it is |
|------|------------|
| `emergency_qr.py` | Proof of concept: signed, expiring Emergency QR link |
| `prescription_ocr.py` | Proof of concept: reads text from a prescription photo |
| `Mockup*.jpeg` | Concept UI mockups (sample data, not a running app) |
| `requirements.txt` | Python libraries needed |

## How to run the scripts
1. Install Python 3.10 or newer.
2. Install the libraries: `pip install -r requirements.txt`
3. QR demo: `python emergency_qr.py` (creates `emergency_qr.png`)
4. OCR demo: install the Tesseract program first (Windows installer from the UB Mannheim Tesseract page), then run `python prescription_ocr.py your_image.jpg`

## Status
Idea stage. The full app (locker, backend, AI summary, multilingual output) is **not built yet**. Only the two small proof-of-concept scripts above exist.

## Team
Poorvi Rao, Saniya S, Swarna M Adyanthaya, Yashaswini

## Disclaimer
AI summaries are an aid, not medical advice. Always follow your doctor's instructions.
