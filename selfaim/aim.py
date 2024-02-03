import pprint

import numpy as np
from PIL import Image, ImageGrab
import cv2
import keyboard
import win32api
import pydirectinput
from ultralytics import YOLO
import torch

model = YOLO("yolov8m.pt")


def pil_grab():
    game_frame = ImageGrab.grab(bbox=(0, 0, 1600, 900))
    game_frame_np = cv2.cvtColor(np.array(game_frame), cv2.COLOR_RGB2BGR)
    results = model(game_frame_np)
    image = results[0].plot()
    print("v8_results: ", results[0].names)

    boxes = results[0].boxes.data
    print(boxes)
    # foramtted_boxes = []
    # for box in boxes:
    #     # foramtted_box = [float(f"{num:.2f}") for num in boxes.tolist()]
    #     foramtted_box = [float(num) for num in boxes.tolist()]
    #     foramtted_boxes.append(foramtted_box)
    # pprint.pprint(foramtted_boxes)

    return image, boxes


if __name__ == "__main__":
    while True:
        x, y = pydirectinput.position()
        print("当前鼠标坐标：", x, y)
        image, formatted_boxes = pil_grab()

        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("result", 500, 300)
        cv2.imshow("result", image)

        cv2.setWindowProperty("result", cv2.WND_PROP_TOPMOST, 1)

        cv2.waitKey(1)
