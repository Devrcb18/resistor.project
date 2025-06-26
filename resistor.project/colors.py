import cv2 as cv

# HSV ranges for resistor color detection
Colour_Range = [
    [(0, 0, 0), (180, 255, 50), "BLACK", 0, (0, 0, 0)],
    [(0, 90, 10), (15, 250, 100), "BROWN", 1, (19, 69, 139)],
    [(0, 70, 50), (10, 255, 255), "RED", 2, (0, 0, 255)],
    [(160, 70, 50), (180, 255, 255), "RED", 2, (0, 0, 255)],
    [(5, 150, 150), (15, 235, 250), "ORANGE", 3, (0, 128, 255)],
    [(20, 100, 100), (30, 255, 255), "YELLOW", 4, (0, 255, 255)],
    [(30, 20, 20), (90, 255, 255), "GREEN", 5, (0, 255, 0)],
    [(100, 150, 0), (140, 255, 255), "BLUE", 6, (255, 0, 0)],
    [(120, 40, 100), (140, 250, 220), "VIOLET", 7, (255, 0, 127)],
    [(15, 80, 120), (35, 255, 255), "GOLD", -1, (0, 215, 255)],
    [(0, 0, 150), (180, 40, 240), "SILVER", -2, (192, 192, 192)],
]

FONT = cv.FONT_HERSHEY_SIMPLEX
min_area = 20

def validContours(cont):
    area = cv.contourArea(cont)
    if area < min_area or area > 3000:
        return False
    x, y, w, h = cv.boundingRect(cont)
    aspect_ratio = float(w) / h
    if h == 0 or w == 0 or aspect_ratio > 1.0:
        return False
    return True