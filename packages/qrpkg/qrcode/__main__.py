import qrcode
import base64
import io
from typing import Any

def main(data:Any)->str:
    """
    Generates a QR code image based on the provided data and returns it as a base64-encoded data URI.

    Args:
    - data (Any): The input data to be encoded into the QR code.

    Returns:
    - str: A base64-encoded data URI representing the generated QR code image.

    The function generates a QR code using the provided data using the qrcode library.
    It converts the generated QR code image to a base64-encoded data URI and returns it.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64-encoded data URI
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    data_uri = f"data:image/png;base64,{img_str}"

    return data_uri