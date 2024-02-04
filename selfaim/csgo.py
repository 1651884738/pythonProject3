# https://pypi.tuna.tsinghua.edu.cn/simple
import pprint

import torch

import numpy as np
import win32api
from PIL import Image, ImageGrab
import cv2
import pydirectinput
from ultralytics import YOLO

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = YOLO("yolov8m.pt").to(device)

screen_width = 1920
screen_height = 1080


def pil_grab():
    game_frame = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    game_frame_np = cv2.cvtColor(np.array(game_frame), cv2.COLOR_RGB2BGR)
    results = model(game_frame_np)
    image = results[0].plot()
    # print("v8_results: ", results[0].names)

    boxes = results[0].boxes.data
    # print(boxes)
    foramtted_boxes = []
    for box in boxes:
        foramtted_box = [float(f"{num:.2f}") for num in box.tolist()]
        # foramtted_box = [float(num) for num in boxes.tolist()]
        foramtted_boxes.append(foramtted_box)
    pprint.pprint(foramtted_boxes)

    return image, foramtted_boxes


def positions(pos):
    x_0 = pos[0]
    y_0 = pos[1]
    x_1 = pos[3]
    y_1 = pos[4]
    x_mid = x_1 - (x_1 - x_0) / 2
    y_mid = y_1 - (y_1 - y_0) / 2
    x_pos = int(x_mid - 965)
    y_pos = int(y_mid - 572)
    print(x_pos, y_pos, x_mid, y_mid)
    return x_mid, y_mid, x_pos, y_pos


if __name__ == "__main__":
    while True:
        x, y = pydirectinput.position()
        print("当前鼠标坐标：", x, y)
        image, formatted_boxes = pil_grab()

        if len(formatted_boxes) > 0:
            indices = [index for index, item in enumerate(formatted_boxes) if (item[-1] == 0.0 and item[-2] > 0.7)]
            print("index: ", indices)

            if len(indices) > 0 and win32api.GetKeyState(0x14) & 0x0001:
                x_mid, y_mid, x_pos, y_pos = positions(formatted_boxes[indices[0]])
                pydirectinput.moveRel(int(x_pos), int(y_pos))

        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("result", 500, 300)
        cv2.imshow("result", image)
        cv2.setWindowProperty("result", cv2.WND_PROP_TOPMOST, 1)
        cv2.waitKey(1)
