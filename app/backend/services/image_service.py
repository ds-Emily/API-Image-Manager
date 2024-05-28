import base64
from io import BytesIO
from PIL import Image
import requests

class ImageProcessor:
    def __init__(self, image_url):
        self.image_url = image_url

    def get_image_data(self):
        response = requests.get(self.image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
