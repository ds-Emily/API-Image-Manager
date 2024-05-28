import base64
from io import BytesIO
from PIL import Image
import requests

class ImageProcessor:
    def __init__(self, image_path=None):
        self.image_path = image_path

    def get_image_data(self):
        response = requests.get(self.image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')

    def get_image_data_from_file(self):
        with open(self.image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string