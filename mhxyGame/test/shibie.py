import pytesseract
from PIL import Image


class Identify():
    def __init__(self):
        self.rect = pytesseract

    def discern(self, image):
        text = pytesseract.image_to_string(image)

        return text
