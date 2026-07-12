import pygame
import tkinter as tk

top_run = False

pygame.init()
screen = pygame.display.set_mode((800, 600))

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
# root.attributes('-fullscreen', True)
root.attributes('-transparentcolor', "#f0f0f0")

menu_options = ["选项 1", "选项 2", "选项 3", "选项 4"]

def on_option_click(option):
    print(f"你点击了 {option}")

def rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


while True:
    info = pygame.display.Info()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            root.destroy()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if top_run:
                    top_run = False
                    top.destroy()
                x, y = root.winfo_pointerx(), root.winfo_pointery()
                top = tk.Toplevel(root)
                top.geometry("+{}+{}".format(x, y))
                top.overrideredirect(True)
                top.attributes('-topmost', True)
                top.attributes('-transparentcolor', "#f0f0f0")

                item_height = 30
                vertical_padding = 20
                menu_height = len(menu_options) * item_height + vertical_padding

                canvas = tk.Canvas(top, width=200, height=menu_height)
                canvas.pack(fill="both", expand=True)

                padding = 10
                radius = 20
                rounded_rect(canvas, padding, padding, 200 - padding, menu_height - padding, radius=radius,
                             fill="#333333")

                item_ids = []
                rect_ids = []
                for i, option in enumerate(menu_options):
                    item_id = canvas.create_text(100, i * item_height + vertical_padding // 2 + item_height // 2,
                                                 text=option, fill="white", font=("Arial", 12))
                    item_ids.append(item_id)

                    rect_id = canvas.create_rectangle(padding, i * item_height + vertical_padding // 2,
                                                      200 - padding, i * item_height + vertical_padding // 2 + item_height,
                                                      fill="", outline="")
                    rect_ids.append(rect_id)

                    def on_enter(event, item=item_id):
                        canvas.itemconfig(item, fill="#00aaff")

                    def on_leave(event, item=item_id):
                        canvas.itemconfig(item, fill="white")

                    def on_click(event, opt=option):
                        canvas.itemconfig(item_id, fill="#00ff00")
                        on_option_click(opt)
                        top.destroy()
                        global top_run
                        top_run = False

                    canvas.tag_bind(rect_id, "<Enter>", on_enter)
                    canvas.tag_bind(rect_id, "<Leave>", on_leave)
                    canvas.tag_bind(rect_id, "<Button-1>", on_click)

                top_run = True
            if event.button == 1:
                if top_run:
                    top_run = False
                    top.destroy()

    screen.fill((255, 255, 255))
    root.update()
    if top_run:
        top.update()

    pygame.display.update()