import tkinter as tk
import json
from macro_system import start_macro, stop_macro


def start_macro_callback():
    start_macro()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)


def stop_macro_callback():
    stop_macro()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)


def save_values():
    data = {
        "value1": spinbox_var1.get(),
        "value2": spinbox_var2.get(),
        "value3": spinbox_var3.get(),
        "value4": spinbox_var4.get(),
        "value5": spinbox_var5.get(),
        "value6": spinbox_var6.get(),
    }
    with open("data.json", "w") as f:
        json.dump(data, f)


def load_values():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            spinbox_var1.set(data.get("value1", 1))
            spinbox_var2.set(data.get("value2", 1))
            spinbox_var3.set(data.get("value3", 1))
            spinbox_var4.set(data.get("value4", 1))
            spinbox_var5.set(data.get("value5", 1))
            spinbox_var6.set(data.get("value6", 1))
            update_values()
    except FileNotFoundError:
        pass


def update_values():
    selected_value1 = spinbox_var1.get()
    value_label1.config(text=f"q 쿨타임: {selected_value1}")

    selected_value2 = spinbox_var2.get()
    value_label2.config(text=f"w 쿨타임: {selected_value2}")

    selected_value3 = spinbox_var3.get()
    value_label3.config(text=f"e 쿨타임: {selected_value3}")

    selected_value4 = spinbox_var4.get()
    value_label4.config(text=f"r 쿨타임: {selected_value4}")

    selected_value5 = spinbox_var5.get()
    value_label5.config(text=f"x 쿨타임: {selected_value5}")

    selected_value6 = spinbox_var6.get()
    value_label6.config(text=f"a 쿨타임: {selected_value6}")


root = tk.Tk()
root.title("메이플 매크로 by Riho")

start_button = tk.Button(root, text="Start Macro", command=start_macro_callback)
start_button.grid(row=0, column=0, pady=5, padx=10)

stop_button = tk.Button(
    root, text="Stop Macro", command=stop_macro_callback, state=tk.DISABLED
)
stop_button.grid(row=1, column=0, pady=5, padx=10)

# Spinbox 값 저장을 위한 IntVar
spinbox_var1 = tk.DoubleVar()
spinbox_var2 = tk.DoubleVar()
spinbox_var3 = tk.DoubleVar()
spinbox_var4 = tk.DoubleVar()
spinbox_var5 = tk.DoubleVar()
spinbox_var6 = tk.DoubleVar()

# Spinbox 생성 (정수 값만 받도록 설정)
value_label1 = tk.Label(root, text="q 쿨타임: ")
value_label1.grid(row=0, column=1, pady=5)
spinbox1 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var1,
    command=update_values,
    wrap=True,
)
spinbox1.grid(row=0, column=2, pady=5)


value_label2 = tk.Label(root, text="w 쿨타임: ")
value_label2.grid(row=1, column=1, pady=5)
spinbox2 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var2,
    command=update_values,
    wrap=True,
)
spinbox2.grid(row=1, column=2, pady=5)


value_label3 = tk.Label(root, text="e 쿨타임: ")
value_label3.grid(row=2, column=1, pady=5)
spinbox3 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var3,
    command=update_values,
    wrap=True,
)
spinbox3.grid(row=2, column=2, pady=5)

value_label4 = tk.Label(root, text="r 쿨타임: ")
value_label4.grid(row=3, column=1, pady=5)
spinbox4 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var4,
    command=update_values,
    wrap=True,
)
spinbox4.grid(row=3, column=2, pady=5)


value_label5 = tk.Label(root, text="x 쿨타임: ")
value_label5.grid(row=4, column=1, pady=5)
spinbox5 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var5,
    command=update_values,
    wrap=True,
)
spinbox5.grid(row=4, column=2, pady=5)


value_label6 = tk.Label(root, text="a 쿨타임: ")
value_label6.grid(row=5, column=1, pady=5)
spinbox6 = tk.Spinbox(
    root,
    from_=0.5,
    to=60,
    increment=0.5,
    width=5,
    textvariable=spinbox_var6,
    command=update_values,
    wrap=True,
)
spinbox6.grid(row=5, column=2, pady=5)

# 값 저장 버튼
save_button = tk.Button(root, text="값 저장", command=save_values)
save_button.grid(row=6, column=1, pady=5)

# 값 불러오기 버튼
load_button = tk.Button(root, text="값 불러오기", command=load_values)
load_button.grid(row=6, column=2, pady=5)


# 앱 실행 시 초기 데이터 로드
load_values()

root.mainloop()
