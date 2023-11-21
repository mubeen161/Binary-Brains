import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Continue with capturing frames
    ret, img = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
    else:
        cv2.rectangle(img, pt1=(280, 180), pt2=(380, 330), color=(0, 255, 0), thickness=5)
        cv2.imshow("hello",img)

        # Taking screenshot
        k = cv2.waitKey(1) & 0xFF
        if k == 13:  # Enter key
            test = "test_finger.bmp"
            cv2.imwrite(test, img)

        cap.release()

        # Rest of your code remains unchanged

        # Assuming you have 'result' and 'crop_img' defined in the rest of your code
        # Replace the final cv2.imshow() calls with cv2_imshow()
        # cv2.imshow("result", result)
        # cv2.imshow('f_print', crop_img)
        # cv2.show("okay",result)
        # cv2.imshow("k",crop_img)

        # ... (rest of your code)

cv2.waitKey(0)
cv2.destroyAllWindows()