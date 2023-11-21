from aip import AipOcr
from PIL import ImageGrab
import time

class Identify():
    """
    OCR识别图片文字
    """

    # img = Image.open('number-example.png')
    # config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
    # print(pytesseract.image_to_string(img, config=config))
    def __init__(self):
        self.APP_ID = '43257106'
        self.API_KEY = 'B4fzZ7ltiK6TWW3VkOnujO0p'
        self.SECRET_KEY = 'GaCIaxKPbGLTFsyZMkKNOzKSGxAmCOMY'

        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def screens(self):
        # 屏幕截图
        screen = ImageGrab.grab(bbox=(1090, 310, 1278, 443))  # 指定位置的坐标 (x1, y1) 到 (x2, y2)
        # 进行图像二值化
        screen.save("D:/狂神java/pythoncode/PythonStudy/mhxyGame/project_mhxy/images/saveImg/todo.png")

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_text(self):
        self.screens()
        time.sleep(0.5)
        image = self.get_file_content("D:/狂神java/pythoncode/PythonStudy/mhxyGame/project_mhxy/images/saveImg/todo.png")
        result = self.client.basicGeneral(image)  # 调用百度OCR的通用文字识别接口
        for word in result['words_result']:
            print(word['words'])


if __name__ == "__main__":
    demo = Identify()
    demo.get_text()
