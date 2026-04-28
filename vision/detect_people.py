import cv2
import time

from analysis.analyze import analyze_people
from database.db import write_data
from crawler.fake_crawler import get_event_reason

IMAGE_PATH = "vision/classroom.jpg"


def detect_people():
    image = cv2.imread(IMAGE_PATH)

    if image is None:
        print("找不到圖片：", IMAGE_PATH)
        return

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    boxes, weights = hog.detectMultiScale(
        image,
        winStride=(8, 8),
        padding=(8, 8),
        scale=1.05
    )

    people_count = len(boxes)
    status = analyze_people(people_count)
    reason = get_event_reason()

    data = {
        "classroom": "A101",
        "people_count": people_count,
        "status": status,
        "reason": reason
    }

    write_data(data)

    print("更新人數:", people_count, "狀態:", status, "原因:", reason)


if __name__ == "__main__":
    while True:
        detect_people()
        time.sleep(5)