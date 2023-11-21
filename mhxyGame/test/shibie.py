import pytesseract
from PIL import ImageGrab
import time
# 设置Tesseract OCR路径（根据你的安装路径进行设置）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    # 屏幕截图
    screen = ImageGrab.grab(bbox=(1090, 310, 1278, 443))  # 指定位置的坐标 (x1, y1) 到 (x2, y2)

    # 将截图转换成灰度图像并保存（这一步是可选的）
    gray_screen = screen.convert('L')
    gray_screen.save('gray_screen.png')

    # 识别文本
    custom_config = r'--oem 3 --psm 6'  # 自定义配置，根据实际情况进行调整
    text = pytesseract.image_to_string(gray_screen, config=custom_config)
    # text = pytesseract.image_to_string(gray_screen, lang='chi_sim')

    # 输出识别结果
    print(text)

    break