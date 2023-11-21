# import cv2
# import numpy as np
# from google.colab.patches import cv2_imshow

# cap = cv2.VideoCapture(0)  # Open the default camera (Webcam)

# # Fingerprint capturing loop
# while True:
#     ret, img = cap.read()
#     cv2.rectangle(img, pt1=(280, 180), pt2=(380, 330), color=(0, 255, 0), thickness=5)

#     cv2_imshow(img)  # Display the video frame in Colab

#     # Taking screenshot when 'Enter' key is pressed
#     k = cv2.waitKey(1) & 0xFF
#     if k == 13:
#         test = "test_finger.bmp"
#         cv2.imwrite(test, img)
#         break

# cap.release()

# # Read the captured fingerprint image
# img = cv2.imread('test_finger.bmp', 1)

# # Preprocess the fingerprint image
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# kernel_sharpening = np.array([[-1, -1, -1],
#                               [-1, 9, -1],
#                               [-1, -1, -1]])
# img = cv2.filter2D(img, -1, kernel_sharpening)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                              cv2.THRESH_BINARY, 11, 2)

# # Crop the fingerprint image
# crop_img = th3[180:330, 280:380]
# test1 = "test_finger1.bmp"
# test2 = "final_finger.bmp"
# crop = cv2.resize(crop_img, (100, 150), interpolation=cv2.INTER_CUBIC)
# cv2.imwrite(test1, th3)
# cv2.imwrite(test2, crop)


import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture(0)  # Open the default camera (Webcam)

# Fingerprint capturing loop
while True:
    ret, img = cap.read()

    if not ret:
        print("Failed to capture frame. Exiting.")
        break

    cv2.rectangle(img, pt1=(280, 180), pt2=(380, 330), color=(0, 255, 0), thickness=5)

    cv2.imshow("k",img)  # Display the video frame in Colab

    # Taking screenshot when 'Enter' key is pressed
    k = cv2.waitKey(1) & 0xFF
    if k == 13:
        test = "test_finger.bmp"
        cv2.imwrite(test, img)
        break

cap.release()

# Read the captured fingerprint image
img = cv2.imread('test_finger.bmp', 1)

# Preprocess the fingerprint image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
img = cv2.filter2D(img, -1, kernel_sharpening)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 11, 2)

# Crop the fingerprint image
crop_img = th3[180:330, 280:380]
test1 = "test_finger1.bmp"
test2 = "final_finger.bmp"
crop = cv2.resize(crop_img, (100, 150), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(test1, th3)
cv2.imwrite(test2, crop)

# Display preprocessed and cropped images in Colab
cv2.imshow("ll",th3)
cv2.imshow("p",crop)

# ... (rest of your code)



# # Display preprocessed and cropped images in Colab
# cv2_imshow(th3)
# cv2_imshow(crop)

# Fingerprint Matching (Currently Commented Out)
fingerprint_database_image = cv2.imread("Abhishek.bmp")
sift = cv2.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(crop_img, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)
matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                dict()).knnMatch(descriptors_1, descriptors_2, k=2)
match_points = []

for p, q in matches:
    if p.distance <= 0.9 * q.distance:
        match_points.append(p)

keypoints = min(len(keypoints_1), len(keypoints_2))

if (len(match_points) / keypoints * 100 >= 0):
    print("Fingerprint match accuracy: ", (len(match_points) / keypoints) * 100)
    result = cv2.drawMatches(crop_img, keypoints_1, fingerprint_database_image,
                             keypoints_2, match_points, None)
    result = cv2.resize(result, None, fx=2, fy=2)
    cv2.imshow("llll",result)  # Display the matching result in Colab
else:
    print("Fingerprint does not match.")