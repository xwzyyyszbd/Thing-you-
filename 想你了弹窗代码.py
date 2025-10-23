import tkinter as tk
import random

messages = [
    ("我想你了!", "pink"),
    ("别熬夜", "skyblue"),
    ("每天都要开开心心", "lightyellow")
]


def create_single_popup():
    popup = tk.Toplevel(root)
    popup.title("温馨提示")  # 保留标题

    # 随机选择信息和背景色
    msg, bg_color = random.choice(messages)
    popup.config(bg=bg_color)  # 弹窗背景与内容色一致

    # 标签设置（适配240x50尺寸）
    label = tk.Label(
        popup,
        text=msg,
        bg=bg_color,
        font=("楷体", 16),
        padx=20,
        pady=5,
        wraplength=200
    )
    label.pack()

    # 固定尺寸（宽度240，高度50）
    popup.geometry("240x50")

    # 随机位置（确保在屏幕内）
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(50, screen_width - 240 - 50)
    y = random.randint(50, screen_height - 50 - 50)
    popup.geometry(f"240x50+{x}+{y}")


def loop_create(count):
    if count > 0:
        create_single_popup()
        # 保持200ms间隔，避免创建过快导致卡顿
        root.after(200, loop_create, count - 1)
    else:
        print("所有弹窗创建完成（约100个）")


root = tk.Tk()
root.withdraw()
root.update_idletasks()
loop_create(100)  # 直接设置为100个弹窗
root.mainloop()