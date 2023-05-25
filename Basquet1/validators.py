from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_size(image):
    img = Image.open(image)
    width, height = img.size
    if width > 500 or height > 500:
        raise ValidationError("Max avatar size is 500x500 pixels")