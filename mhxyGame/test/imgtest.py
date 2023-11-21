from PIL import ImageGrab
from shibie import Identify
import pytesseract
class ScreenShot():
    def __init__(self):
        self.screenshot = ImageGrab

    def shotAll(self):
        screenshot = self.screenshot.grab()
        return screenshot

    def shot_everywhere(self, name):
        # 指定截图区域的坐标
        bbox = (1270, 578, 1440, 700)
        screenshot = self.screenshot.grab(bbox)
        screenshot.save(f"D:/狂神java/pythoncode/PythonStudy/mhxyGame/project_mhxy/images/saveImg/{name}.png")


if __name__ == "__main__":
    # import pytesseract
    # s = ScreenShot()
    #
    # s.shot_everywhere("test")
    import pytesseract
    from PIL import Image

    # 打开图像文件
    image = Image.open("test.png")

    # 使用Pytesseract进行文字识别
    text = pytesseract.image_to_string(image)

    # 打印识别结果
    print(text)