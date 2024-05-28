from browser import ajax, timer
from components.image_display import update_image

def fetch_new_image():
    def on_complete(req):
        if req.status == 200:
            data = req.json()
            update_image(data['image_data'])

    ajax.get('/api/image', oncomplete=on_complete)

def start_background_change(interval=5000):
    fetch_new_image()
    timer.set_interval(fetch_new_image, interval)
