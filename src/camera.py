import cv2
import numpy as np


def scan(img):
    blur = cv2.GaussianBlur(img, (5,5), 0)
    scan_line = blur[0:, 25:26]

    lower_color_bound = (90, 110, 120)
    upper_color_bound = (255, 255, 255)

    mask = cv2.inRange(scan_line, lower_color_bound, upper_color_bound)
    output = cv2.bitwise_and(scan_line, scan_line, mask=mask)

    non_zero = np.nonzero(output)
    result = []
    for i in non_zero[0]:
        if i not in result:
            result.append(i)

    # cv2.imshow("img", blur)
    # cv2.imshow("output", output)
    # cv2.imshow("scan_line", scan_line)
    cv2.waitKey()

    return result
