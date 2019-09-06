#!/usr/bin/env python3
# coding: utf8
"""
    Author: freezed <git@freezed.me> 2019-09-06
    Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/
"""

import io
import base64
from PIL import Image


def main(source_img_b64_str, height=100, width=100):
    """
        Resize a Base64 string image

        :param source_img_b64_str:
        :param height: new height in pixel
        :param width: new width in pixel
        :type source_img_b64_str: str A full Base64 encoded image (PNG)
        :type height: int
        :type width: int
        :return: The same image resized Base64 encoded
        :rtype: str

        :Tests:
        >>> src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAS4AAACYCAYAAABapASfAAAA5klEQVR4nO3UsQ2AMBAEwe2U778JSCjAkS3QjHT5RVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwP1Ndp08ArJrqfjdHnwAsmoQL+KBJtAAAAAAAAAAAAAAAAAAAYIsHJxwG/A1QeRMAAAAASUVORK5CYII="
        >>> main(src)
        'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAATUlEQVR4nO3OQQ0AMAgEMJxu/k3AGwWXbK2CVgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAo046wNbpANtNBwAAAH42ANwBv4bl/B8AAAAASUVORK5CYII='
    """

    head_b64_str = source_img_b64_str.split(",")[0]
    body_b64_str = source_img_b64_str.split(",")[1]

    body_b64_bytes = base64.b64decode(body_b64_str)
    body_file_like = io.BytesIO(body_b64_bytes)
    body_pil_image = Image.open(body_file_like)

    resized_body_pil_image = body_pil_image.resize((height, width))

    new_img_bytes = io.BytesIO()
    resized_body_pil_image.save(new_img_bytes, format="PNG")
    new_img_bytes = new_img_bytes.getvalue()

    new_body_b64_str = base64.b64encode(new_img_bytes).decode()

    return "{},{}".format(head_b64_str, new_body_b64_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
