# -*- coding: utf-8 -*-
import ctypes
import random
import pyautogui
import win32con
import win32gui


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle


def _move_click(ratio_x, ratio_y, x1, x2, y1, y2):
    xx = ratio_x * (x2 - x1) + x1
    yy = ratio_y * (y2 - y1) + y1
    pyautogui.moveTo(xx, yy)
    pyautogui.click()


if __name__ == '__main__':
    (x1, y1, x2, y2), handle = get_window_pos('原神')
    if handle:
        win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        win32gui.SetForegroundWindow(handle)
        if x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
            pyautogui.hotkey('altleft', 'enter')
    (x1, y1, x2, y2), handle = get_window_pos('原神')
    if handle:
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        curr_window = user32.GetForegroundWindow()
        while True:
            (x11, y11, x21, y21), handle = get_window_pos('原神')
            if handle:
                if x1 != x11 or y2 != y21:
                    pyautogui.sleep(0.5)
                    continue
                rdm = random.random()
                while rdm < 0.4: rdm += 0.1
                while rdm > 0.6: rdm -= 0.1
                pyautogui.sleep(rdm)
                print("click after", rdm)
                _move_click(0.6954, 0.7531, x1, x2, y1, y2)
