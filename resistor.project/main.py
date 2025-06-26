import cv2 as cv
import numpy as np
from colors import FONT
from bands import findBands, fix_band_order, mouse_callback

def displayResults(sortedbands):
    if len(sortedbands) in [3, 4, 5]:
        strvalue = ""
        for band in sortedbands[:-1]:
            if band[3] >= 0:
                strvalue += str(band[3])
        if not strvalue.isdigit():
            print("Detected bands are not valid for resistance calculation.")
            print("Detected:", [(b[2], b[3]) for b in sortedbands])
            return None
        intvalue = int(strvalue)
        intvalue *= 10 ** sortedbands[-1][3]
        print("Detected Bands:", [(b[2], b[3]) for b in sortedbands])
        print(f"The Resistance is :{intvalue}Ω")
        return intvalue
    else:
        print("Could not detect correct number of bands.")
        print("Detected:", [(b[2], b[3]) for b in sortedbands])
        return None

if __name__ == '__main__':
    image = cv.imread(r"C:\python\resistor.project\testresistor.jpg")

    if image is None:
        print("Error: Image not found.")
    else:
        image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        cv.namedWindow("Resistor with Value")
        cv.setMouseCallback("Resistor with Value", mouse_callback, param=image_hsv)

        sortedbands = findBands(image)
        if sortedbands is not None:
            sortedbands = fix_band_order(sortedbands)
            val = displayResults(sortedbands)

            if val is not None:
                font_scale = 1.2
                font_thickness = 2
                color = (255, 255, 255)

                min_y = min(b[1] for b in sortedbands)
                x_center = int(np.mean([b[0] for b in sortedbands]))
                y_pos = max(30, min_y - 20)

                text = f"{val} ohm"
                cv.putText(image, text, (x_center - 70, y_pos), FONT, font_scale, color, font_thickness, cv.LINE_AA)

        cv.imshow("Resistor with Value", image)
        cv.waitKey(0)
        cv.destroyAllWindows()