import cv2
import json
import time

IMAGE_PATH = "vision/classroom.jpg"
DATA_PATH = "data.json"


def detect_people():
    # 讀取圖片
    image = cv2.imread(IMAGE_PATH)

    if image is None:
        print("找不到圖片：", IMAGE_PATH)
        return

    # OpenCV 內建 HOG 人體偵測器
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # 偵測人
    boxes, weights = hog.detectMultiScale(
        image,
        winStride=(8, 8),
        padding=(8, 8),
        scale=1.05
    )

    people_count = len(boxes)

    # 判斷狀態
    if people_count < 5:
        status = "偏少"
    elif people_count < 15:
        status = "普通"
    else:
        status = "擁擠"

    # 要寫入 data.json 的資料
    data = {
        "classroom": "A101",
        "people_count": people_count,
        "status": status
    }

    # 寫入 data.json
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("更新人數:", people_count, "狀態:", status)


if __name__ == "__main__":
    while True:
        detect_people()
        time.sleep(5)