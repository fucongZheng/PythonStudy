import pyautogui
from PIL import ImageGrab
import math
import threading
import time

# 目标颜色
target_color = [(8, 8, 8),(224,116,32),(144,44,40),(240,148,128),(176,68,56)]  # 举例：目标颜色为红色

# 颜色匹配的容差范围
def color_distance(c1, c2):
    return math.sqrt(sum([(c1[i] - c2[i]) ** 2 for i in range(3)]))

# 线程执行的函数
def color_check_thread():
    while True:
        screenshot = ImageGrab.grab()
        x, y = pyautogui.position()  # 获取当前鼠标位置
        color = screenshot.getpixel((x, y))  # 获取当前鼠标位置的颜色dsfsdfdsfsd是的发水电费水电费都是
        # 判断颜色是否匹配
        for i in target_color:
            if color_distance(color, i) < 10:  # 设置一个合适的阈值
                # 执行点击操作
                print('找到了')
                pyautogui.doubleClick(x, y)


# 创建并启动线程
color_check_thread = threading.Thread(target=color_check_thread)
color_check_thread.daemon = True  # 将线程设置为守护线程，这样在主程序结束时会自动关闭
color_check_thread.start()

# 主程序继续执行其他任务
while True:
    # 这里可以编写主程序需要执行的其他任务
    time.sleep(10)  # 示例：这里让主程序每隔一秒执行一次其他任务
    pyautogui.click(1041, 720)
    break
