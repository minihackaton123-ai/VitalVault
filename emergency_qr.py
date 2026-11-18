"""VitalVault: Emergency QR proof of concept.

Creates a signed, expiring link and turns it into a QR code image.
The QR does NOT contain health data. It only holds a link with a signed
token. A backend (not built yet) would check the token and show a
read-only page with the patient's critical info.

Run:
    python emergency_qr.py
"""
import base64
import hashlib
import hmac
import os
import time

SECRET = os.environ.get("VITALVAULT_SECRET", "demo-secret-change-me").encode()
BASE_URL = "https://example.com/emergency"  # placeholder address


def make_token(patient_id: str, valid_minutes: int = 60) -> str:
    """Create a token that is signed and expires after valid_minutes."""
    expiry = int(time.time()) + valid_minutes * 60
    payload = f"{patient_id}.{expiry}"
    sig = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()[:32]
    return base64.urlsafe_b64encode(f"{payload}.{sig}".encode()).decode()


def verify_token(token: str):
    """Return (True, patient_id) if valid, or (False, reason) if not."""
    try:
        raw = base64.urlsafe_b64decode(token.encode()).decode()
        patient_id, expiry, sig = raw.rsplit(".", 2)
    except Exception:
        return False, "Invalid token"
    expected = hmac.new(SECRET, f"{patient_id}.{expiry}".encode(), hashlib.sha256).hexdigest()[:32]
    if not hmac.compare_digest(sig, expected):
        return False, "Invalid signature"
    if time.time() > int(expiry):
        return False, "Link expired"
    return True, patient_id


def make_qr(url: str, filename: str = "emergency_qr.png") -> str:
    import qrcode  # installed with: pip install -r requirements.txt

    qrcode.make(url).save(filename)
    return filename


if __name__ == "__main__":
    token = make_token("patient001", valid_minutes=60)
    url = f"{BASE_URL}/{token}"
    print("Link:", url)
    print("QR saved as:", make_qr(url))
    print("Check token:", verify_token(token))
    print("Tampered token:", verify_token(token[:-2] + "xx"))
