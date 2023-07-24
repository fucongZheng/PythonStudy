from PIL import ImageGrab


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
        screenshot.save(f"./saveImg/{name}.png")
