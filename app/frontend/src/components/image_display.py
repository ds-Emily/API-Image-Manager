from browser import document

def update_image(image_data):
    image_element = document['remote-image']
    image_element.attrs['src'] = f"data:image/jpeg;base64,{image_data}"
