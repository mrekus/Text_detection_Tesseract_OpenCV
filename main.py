import cv2
import pytesseract

# Nurodomas kelias iki Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract\\tesseract.exe"

# Nustatomas šriftas OpenCV tekstui
font_scale = 2
font = cv2.FONT_HERSHEY_PLAIN

# Nustatomas vaizdo šaltinis
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open camera")

# Paleidžiamas ciklas kuris skaito kiekvieną video kadrą
while True:
    ret, frame = cap.read()
    imgW, imgH, _ = frame.shape
    x1, y1, w1, h1 = 0, 0, imgW, imgH

    img2char = pytesseract.image_to_string(frame)
    img_boxes = pytesseract.image_to_boxes(frame)
    for box in img_boxes.splitlines():
        dimensions = box.split()
        x, y, w, h = int(dimensions[1]), int(dimensions[2]), int(dimensions[3]), int(dimensions[4])
        cv2.rectangle(frame, (x, imgW - y), (w, imgW - h), (255, 0, 0), 2)

    cv2.putText(frame, img2char, (x1 + int(w1/50), y1 + int(h1/30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Camera feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
