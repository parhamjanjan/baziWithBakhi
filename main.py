import cv2
import numpy as np
import pyautogui

def detect_main_color(frame):
    a=1
    # تبدیل فریم از فضای رنگی BGR به HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # محاسبه میانگین رنگ در کانال‌های مختلف برای فریم
    red_mean = np.mean(frame[:, :, 2])  # کانال قرمز (R)
    green_mean = np.mean(frame[:, :, 1])  # کانال سبز (G)
    blue_mean = np.mean(frame[:, :, 0])  # کانال آبی (B)

    # تشخیص رنگ‌های مورد نظر بر اساس میانگین‌های محاسبه شده
    if red_mean > 100:  # حد آستانه میانگین رنگ قرمز
          # فشار دادن کلید d

        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        if a==1:
            pyautogui.keyDown('w')
        a=0
        return "red"
    elif green_mean > 100: 
        pyautogui.keyUp('a')
        pyautogui.keyUp('d') 
        if a==1:
            pyautogui.keyDown('w')
        a=0
        return "green"
    elif blue_mean > 100:  # حد آستانه میانگین رنگ آبی
        pyautogui.keyUp('d')
        pyautogui.keyDown('a') # فشار دادن کلید w
        if a==1:
            pyautogui.keyDown('w')
        a=0
        return "blue"
        
    else:
        pyautogui.keyUp('a')
        pyautogui.keyUp('d')
        pyautogui.keyUp('w')
        a=1
        return "other"

# باز کردن دوربین وب
video_capture = cv2.VideoCapture(0)

while True:
    # خواندن یک فریم از دوربین وب
    ret, frame = video_capture.read()

    # انجام تشخیص رنگ برای فریم فعلی
    main_colors = detect_main_color(frame)

    # نمایش نتایج بر روی فریم
    cv2.putText(frame, main_colors, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # نمایش فریم
    cv2.imshow('Video', frame)

    # اگر کاربر کلید q را فشار دهد، خروج از حلقه
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزاد کردن منابع
video_capture.release()
cv2.destroyAllWindows()
