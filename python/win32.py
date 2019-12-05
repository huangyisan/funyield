# pip3 install pywin32

import win32gui,win32api, win32con

# hwnd = win32gui.FindWindow(None,'live-Bigdata-jumpbox')
hwnd = win32gui.FindWindow(None,'安全整改')

def get_screen_resolution():
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return x,y

def get_window_pos(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    left+=8
    top+=8
    right-=8
    bottom-=8
    return left, top, right, bottom

def get_window_size(pos):
    left, top, right, bottom = pos
    w = right - left
    h = bottom - top
    return w,h

def window_move_left(resolution, size):
    x,y = resolution
    w,h = size

    half_x = int(x/2)
    # half_y = y/2

    ratio_w = int(w/half_x)
    h = ratio_w * h

    win32gui.MoveWindow(hwnd, -8, 0, half_x, h, True)

# win32gui.MoveWindow(hwnd, -8, 0, 937, 545, True)

# print(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
# print(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

if __name__ == '__main__':
    resolution = get_screen_resolution()
    pos = get_window_pos(hwnd)
    size = get_window_size(pos)
    window_move_left(resolution,size)
