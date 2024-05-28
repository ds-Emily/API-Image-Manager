from flask import Flask, jsonify, render_template
from http_requests.image_api import ImageAPI
from services.image_service import ImageProcessor
import os
import random


app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

IMAGE_API_URL = 'https://example.com/api/images'
POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon'


# Carpeta donde se almacenan las imágenes locales
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'images')


# Función para obtener la información de la imagen
def get_image_data():
    image_api = ImageAPI(IMAGE_API_URL)
    image_url = image_api.fetch_image()

    image_processor = ImageProcessor(image_url)
    image_data = image_processor.get_image_data()

    return image_data


def get_image_from_folder():
    image_file = random.choice(os.listdir(IMAGE_FOLDER))
    image_path = os.path.join(IMAGE_FOLDER, image_file)
    
    image_processor = ImageProcessor(image_path)
    image_data = image_processor.get_image_data_from_file()
    
    return image_data


@app.route('/api/image', methods=['GET'])
def get_image():
    image_data = get_image_from_folder()
    return jsonify({'image_data': image_data})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
