from flask import Flask, jsonify, render_template
from http_requests.image_api import ImageAPI
from services.image_service import ImageProcessor

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

# Endpoint de la API externa que proporciona las imágenes
IMAGE_API_URL = 'https://example.com/api/images'

@app.route('/api/image', methods=['GET'])
def get_image():
    image_api = ImageAPI(IMAGE_API_URL)
    image_url = image_api.fetch_image()
    image_processor = ImageProcessor(image_url)
    image_data = image_processor.get_image_data()
    return jsonify({'image_data': image_data})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
