import pytesseract
import cv2
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


class Identify():
    """
    OCR识别图片文字
    """

    # img = Image.open('number-example.png')
    # config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
    # print(pytesseract.image_to_string(img, config=config))
    def __init__(self):
        self.rect = pytesseract

    def discern(self, image_path):
        image = Image.open(image_path).convert("L")
        # 进行图像二值化
        threshold = 116  # 根据实际情况调整阈值
        binary_image = image.point(lambda p: p > threshold and 255)
        if image is not None:
            # cv2.imshow('result', image)
            # cv2.waitKeyEx(50)
            # config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
            text = pytesseract.image_to_string(binary_image, lang='chi_sim')
            return text

        else:
            print('Failed to load image.')


if __name__ == "__main__":
    import pytesseract
    # s = ScreenShot()
    #
    # s.shot_everywhere("test")
    from PIL import Image

    # 打开彩色图像文件并将其转为灰度图像

    # 使用二值图像进行文字识别
    text = pytesseract.image_to_string(Image.open(r"D:/start/image/6.png"), lang='chi_sim', config='--psm 6')

    print(text)
