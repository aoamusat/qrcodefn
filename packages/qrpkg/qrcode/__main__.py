import qrcode
import base64
import io
from typing import Any, Dict


def main(event, context) -> Dict[str, Any]:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    data = event.get("data", None)
    if data is None:
        data = ""
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64-encoded data URI
    buffered = io.BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    data_uri = f"data:image/png;base64,{img_str}"

    return {
        "body": {
            "qrcode": data_uri,
        }
    }
