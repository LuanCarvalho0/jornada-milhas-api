from io import BytesIO
from PIL import Image
import os
from django.conf import settings


MEDIA_TEST =os.path.join(os.path.dirname(__file__), 'media')


def valid_image() -> None:
        image_file = BytesIO()
        image = Image.open(os.path.join(MEDIA_TEST, 'test-image.jpg')) 
        image.save(image_file, format="PNG")
        image_file.name = 'test-image.png'
        image_file.seek(0)
        return image_file
    
def delete_image_test(pasta) -> None:
    image_path = os.path.join(settings.MEDIA_ROOT, f'{pasta}test-image.png')
    if os.path.exists(image_path):
        os.remove(image_path)