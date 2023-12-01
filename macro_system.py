from pynput.keyboard import Key, Controller
import threading
import time
import json


keyboard = Controller()
running = False  # 키 입력 상태를 나타내는 변수

delay = [30, 30, 30, 30, 30, 30, 30, 30]


def press_q():
    while running:
        keyboard.press("q")
        keyboard.release("q")
        time.sleep(delay[0])


def press_w():
    while running:
        keyboard.press("w")
        keyboard.release("w")
        time.sleep(delay[1])


def press_e():
    while running:
        keyboard.press("e")
        keyboard.release("e")
        time.sleep(delay[2])


def press_r():
    while running:
        keyboard.press("r")
        keyboard.release("r")
        time.sleep(delay[3])


def press_x():
    while running:
        keyboard.press("x")
        keyboard.release("x")
        time.sleep(delay[4])


def press_a():
    while running:
        keyboard.press("a")
        keyboard.release("a")
        time.sleep(delay[5])


# def move_left():
#     while running:
#         keyboard.press(Key.left)
#         time.sleep(10)
#         keyboard.release(Key.left)
#         # keyboard.press("right")
#         # keyboard.release("right")
#         time.sleep(5)


def press_keys():
    global running
    while running:
        # 각 키에 대한 별도의 스레드 생성 및 시작
        thread_q = threading.Thread(target=press_q)
        thread_w = threading.Thread(target=press_w)
        thread_e = threading.Thread(target=press_e)
        thread_r = threading.Thread(target=press_r)
        thread_x = threading.Thread(target=press_x)
        thread_a = threading.Thread(target=press_a)

        thread_q.start()
        thread_w.start()
        thread_e.start()
        thread_r.start()
        thread_x.start()
        thread_a.start()
        # thread_right.start()

        # 각 스레드 종료 대기
        thread_q.join()
        thread_w.join()
        thread_e.join()
        thread_r.join()
        thread_x.join()
        thread_a.join()
        # thread_right.join()


def start_macro():
    global running
    if not running:
        running = True

        json_file_path = "data.json"
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        for i in range(0, 5):
            delay[i] = data.get(f"value{i+1}")

        thread = threading.Thread(target=press_keys)
        thread.start()


def stop_macro():
    global running
    running = False


if __name__ == "__main__":
    # 여기에서는 GUI를 만들지 않고, 위의 기능을 직접 실행하는 코드를 둘 것입니다.
    # 실제 GUI 코드는 다른 파일에서 작성할 예정입니다.
    pass
