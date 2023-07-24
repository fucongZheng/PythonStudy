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
        bbox = (100, 100, 500, 500)
        screenshot = self.screenshot.grab(bbox)
        screenshot.save(f"D:/狂神java/pythoncode/PythonStudy/mhxyGame/project_mhxy/images/saveImg/{name}.png")


if __name__ == "__main__":
    import pytesseract
    # s = ScreenShot()
    #
    # s.shot_everywhere("test")
    from PIL import Image

    # 打开彩色图像文件并将其转为灰度图像



    # 使用二值图像进行文字识别
    text = pytesseract.image_to_string(Image.open(r"D:/start/image/5.png"))

    print(text)