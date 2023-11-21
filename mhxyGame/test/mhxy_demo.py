from pynput import keyboard
import pyautogui
import time

position = False


def on_press(key):
    print('按下键：{}'.format(key))
    global position
    if key in [keyboard.Key.space, keyboard.Key.f4, keyboard.Key.f3]:
        if key not in [keyboard.Key.f4, keyboard.Key.f3]:
            pyautogui.click(1140, 470)
        else:
            if key == keyboard.Key.f4:
                pyautogui.hotkey('alt', 'd')
                time.sleep(0.09)
                pyautogui.hotkey('alt', 'd')
            elif key == keyboard.Key.f3:
                pyautogui.hotkey('alt', 'd')
                time.sleep(0.09)
                pyautogui.hotkey('alt', 'a')


def on_release(key):
    print('释放键：{}'.format(key))
    if key == keyboard.Key.esc:
        # 按下 'esc' 键停止监听
        return False


if __name__ == "__main__":
    # 创建监听器对象并绑定回调函数
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

    # 启动监听器
    listener.start()

    # 程序会持续运行，直到按下 'esc' 键停止监听
    listener.join()
