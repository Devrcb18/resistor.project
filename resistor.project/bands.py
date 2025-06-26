import cv2 as cv
import numpy as np
from colors import Colour_Range, FONT, validContours

def findBands(img):
    img1 = cv.bilateralFilter(img, 40, 90, 90)
    img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img_hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
    thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 79, 2)
    thresh = cv.bitwise_not(thresh)

    bandpos = []

    for clr in Colour_Range:
        mask = cv.inRange(img_hsv, clr[0], clr[1])

        if clr[2] == 'RED':
            red_mask = cv.inRange(img_hsv, (160, 70, 50), (180, 255, 255))
            mask = cv.bitwise_or(red_mask, mask)

        mask = cv.bitwise_and(mask, thresh, mask=mask)

        contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for cont in contours:
            if validContours(cont):
                lmp = tuple(cont[cont[:, :, 0].argmin()][0])
                bandpos.append(lmp + tuple(clr[2:]))

    bandpos = sorted(bandpos, key=lambda tup: tup[0])

    filtered = []
    if bandpos:
        used = [False] * len(bandpos)
        for i, band in enumerate(bandpos):
            if used[i]:
                continue
            cluster = [band]
            used[i] = True
            for j in range(i+1, len(bandpos)):
                if not used[j] and bandpos[j][2] == band[2] and abs(bandpos[j][0] - band[0]) < 40:
                    cluster.append(bandpos[j])
                    used[j] = True
            xs = [b[0] for b in cluster]
            ys = [b[1] for b in cluster]
            color, value, bgr = cluster[0][2], cluster[0][3], cluster[0][4]
            avg_x = int(np.mean(xs))
            avg_y = int(np.mean(ys))
            filtered.append((avg_x, avg_y, color, value, bgr))

    img_w = img.shape[1]
    margin = int(img_w * 0.08)
    filtered = [b for b in filtered if margin < b[0] < img_w - margin]

    if len(filtered) > 4:
        filtered = sorted(filtered, key=lambda tup: tup[0])
        if len(filtered) == 5:
            filtered = filtered[1:4]
        elif len(filtered) == 6:
            filtered = filtered[1:5]
        else:
            start = (len(filtered) - 4) // 2
            filtered = filtered[start:start+4]

    return filtered

def fix_band_order(bands):
    bands = sorted(bands, key=lambda b: b[0])
    if len(bands) == 4:
        if bands[3][3] < 0:
            return bands
        for i in range(3):
            if bands[i][3] < 0:
                tol = bands.pop(i)
                bands.append(tol)
                break
    return bands

def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        hsv_val = param[y, x]
        print(f"HSV at ({x}, {y}): {hsv_val}")