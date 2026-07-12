import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont

class ChatWindow:
    def __init__(self, user_list):
        self.window = tk.Tk()
        self.window.title("Chat Window")
        self.window.geometry("1000x500")

        self.create_styles()
        self.create_left_frame()
        self.create_right_frame()

        self.user_list = user_list
        self.avatar_photos = []  # Create a list to store the avatar photos
        self.create_user_canvas()
        self.selected_user_canvas = None

    def create_styles(self):
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#050B15")
        self.style.configure("TText", background="#050B15", foreground="#fff")

    def create_left_frame(self):
        self.left_frame = ttk.Frame(self.window, width=200, style="TFrame")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

    def create_right_frame(self):
        self.right_frame = ttk.Frame(self.window, width=400, style="TFrame")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_chat_frame()
        self.create_input_frame()

    def create_chat_frame(self):
        self.chat_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.create_chat_canvas()

    def create_chat_canvas(self):
        self.chat_canvas = tk.Canvas(self.chat_frame, width=400, bg="#050B15")
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.chat_frame, command=self.chat_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind the mouse wheel event to the Canvas
        self.chat_canvas.bind("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.chat_canvas.yview_scroll(-1*(event.delta//120), "units")

    def create_input_frame(self):
        self.input_frame = ttk.Frame(self.right_frame, style="TFrame")
        self.input_frame.pack(fill=tk.X)

        self.create_message_text()
        self.create_send_button()

    def create_message_text(self):
        self.message_text = tk.Text(self.input_frame, height=6, bg="#050B15", fg="#fff", font=("Microsoft YaHei",10))
        self.message_text.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_send_button(self):
        self.send_button_canvas = tk.Canvas(self.input_frame, width=60, height=30, bg="#0099ff")
        self.send_button_canvas.pack(side=tk.RIGHT)

        self.send_button_canvas.create_rectangle(0, 0, 60, 30, fill="#0099ff", tags="button")
        self.send_button_canvas.create_text(30, 15, text="发送", fill="#fff", font=("Arial", 12, "bold"), tags="text")

        self.send_button_canvas.tag_bind("button", "<Enter>", lambda event: self.send_button_canvas.itemconfig("button", fill="#007acc"))
        self.send_button_canvas.tag_bind("button", "<Leave>", lambda event: self.send_button_canvas.itemconfig("button", fill="#0099ff"))
        self.send_button_canvas.tag_bind("button", "<Button-1>", lambda event: self.send_button_canvas.itemconfig("button", fill="#005999"))
        self.send_button_canvas.tag_bind("button", "<ButtonRelease-1>", self.send_message)

        self.send_button_canvas.tag_bind("text", "<Enter>", lambda event: self.send_button_canvas.itemconfig("button", fill="#007acc"))
        self.send_button_canvas.tag_bind("text", "<Leave>", lambda event: self.send_button_canvas.itemconfig("button", fill="#0099ff"))
        self.send_button_canvas.tag_bind("text", "<Button-1>", lambda event: self.send_button_canvas.itemconfig("button", fill="#005999"))
        self.send_button_canvas.tag_bind("text", "<ButtonRelease-1>", self.send_message)

    def load_avatar(self, avatar_path, size=None):
        avatar_image = Image.open(avatar_path)
        if size is None:  # If no size is specified, resize the image to 1/5 of its original size
            width, height = avatar_image.size
            size = (width, height)
        avatar_image = avatar_image.resize(size, Image.ANTIALIAS)  # Resize the image to the specified size
        return ImageTk.PhotoImage(avatar_image)
    
    def on_user_enter(self, user_canvas):
        if user_canvas != self.selected_user_canvas:  # Only change the color if the user is not selected
            user_canvas.configure(bg="#d3d3d3")  # Change the background color to light gray

    def on_user_leave(self, user_canvas):
        if user_canvas != self.selected_user_canvas:  # Only change the color if the user is not selected
            user_canvas.configure(bg="#050B15")  # Change the background color back

    def on_user_click(self, user_canvas):
        if self.selected_user_canvas:
            self.selected_user_canvas.configure(bg="#050B15")  # Change the color of the previously selected user back
        user_canvas.configure(bg="#808080")  # Change the background color to dark gray
        self.selected_user_canvas = user_canvas  # Save the selected user canvas

    def create_user_canvas(self):
        for i, user in enumerate(self.user_list):
            user_canvas = tk.Canvas(self.left_frame, width=250, height=50, bg="#050B15")
            user_canvas.pack()

            avatar_photo = self.load_avatar(user["avatar_image"],(50,50))  # Use the default size for user list avatars
            self.avatar_photos.append(avatar_photo)  # Add the avatar photo to the list
            user_canvas.create_image(35, 25, image=avatar_photo)

            username = user["user_name"]
            user_canvas.create_text(120, 15, text=username, font=("Arial", 12, "bold"), fill="#fff")

            latest_message = user["lastest_message"]
            user_canvas.create_text(120, 35, text=latest_message, fill="#fff")

            user_canvas.create_oval(52, 1, 65, 14, fill="blue", outline="blue", tags="blue_dot")
            user_canvas.create_text(58.5, 7.5, text="1", fill="white", font=("Arial", 10, "bold"), tags="blue_dot_text")

            user_canvas.bind("<Enter>", lambda event, canvas=user_canvas: self.on_user_enter(canvas))  # Call the on_user_enter method when the mouse enters
            user_canvas.bind("<Leave>", lambda event, canvas=user_canvas: self.on_user_leave(canvas))  # Call the on_user_leave method when the mouse leaves
            user_canvas.bind("<Button-1>", lambda event, canvas=user_canvas: self.on_user_click(canvas))  # Call the on_user_click method when the user is clicked

            if i < len(self.user_list) - 1:  # Don't add a separator after the last user
                separator = tk.Frame(self.left_frame, height=2, bg="#000")
                separator.pack(fill=tk.X)

    def send_message(self, event):
        message = self.message_text.get("1.0", tk.END).strip()

        if message:
            if message.startswith("img:"):  # Check if the message is an image
                image_path = message[4:].strip()  # Get the image path
                self.add_image_to_chat_canvas(1, "User1", image_path)
                self.add_image_to_chat_canvas(2, "User2", image_path)
            else:
                self.add_message_to_chat_canvas(1, "User1", message, "img.png")
                self.add_message_to_chat_canvas(2, "User2", message, "img.png", "#91d5ff", "#000")

        self.message_text.delete("1.0", tk.END)

    def add_image_to_chat_canvas(self, sender, username, image_path):
        avatar_photo = self.load_avatar("img.png", size=(30, 30))  # Use a smaller size for chat avatars
        self.avatar_photos.append(avatar_photo)  # Add the avatar photo to the list

        message_y = self.chat_canvas.bbox("all")[3] if self.chat_canvas.bbox("all") else 0

        if sender == 1:
            self.chat_canvas.create_image(35, message_y + 45, image=avatar_photo)
            self.chat_canvas.create_text(35, message_y + 15, text=username, font=("Arial", 10, "bold"), fill="#fff")
            image_anchor = "nw"
            image_x = 65
            image_y = message_y + 35
        else:
            self.chat_canvas.create_image(715, message_y + 30, image=avatar_photo, anchor="ne")
            self.chat_canvas.create_text(715, message_y, text=username, font=("Arial", 10, "bold"), fill="#fff", anchor="ne")
            image_anchor = "ne"
            image_x = 670
            image_y = message_y + 35

        image_photo = self.load_avatar(image_path)  # Load the image and resize it to 200x200
        self.avatar_photos.append(image_photo)  # Add the image photo to the list

        self.chat_canvas.create_image(image_x, image_y, image=image_photo, anchor=image_anchor)

        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))  # Update the scroll region
        self.chat_canvas.yview_moveto(1.0)  # Scroll to the bottom

    def add_message_to_chat_canvas(self, sender, username, message, avatar_path, bg="#4b7bec", fg="#fff"):
        avatar_photo = self.load_avatar(avatar_path, size=(30, 30))  # Use a smaller size for chat avatars
        self.avatar_photos.append(avatar_photo)  # Add the avatar photo to the list

        message_y = self.chat_canvas.bbox("all")[3] if self.chat_canvas.bbox("all") else 0

        if sender == 1:
            self.chat_canvas.create_image(35, message_y + 45, image=avatar_photo)
            self.chat_canvas.create_text(35, message_y + 15, text=username, font=("Arial", 10, "bold"), fill="#fff")
            text_anchor = "nw"
            text_x = 65
            text_y = message_y + 35
        else:
            self.chat_canvas.create_image(715, message_y + 30, image=avatar_photo, anchor="ne")
            self.chat_canvas.create_text(715, message_y, text=username, font=("Arial", 10, "bold"), fill="#fff", anchor="ne")
            text_anchor = "ne"
            text_x = 670
            text_y = message_y + 35

        message_text = tk.Text(self.chat_canvas, width=35, wrap="char", bg=bg, fg=fg, font=("Microsoft YaHei", 12), bd=0)
        message_text.insert("1.0", message)

        font = tkFont.Font(family="Microsoft YaHei",size=10)
        line_width = 0
        line = 1
        for char in message:
            if char == "\n":
                line += 1
                line_width = 0
                continue
            char_width = font.measure(char)
            if line_width + char_width > 280:
                line += 1
                line_width = char_width
            else:
                line_width += char_width
        width = font.measure(message)
        message_text.configure(width=width//8+3 if width<280 else 35,height=line)
        message_text.configure(state="disabled")  # Make the Text widget read-only

        self.chat_canvas.create_window(text_x, text_y, window=message_text, anchor=text_anchor)

        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))  # Update the scroll region
        self.chat_canvas.yview_moveto(1.0)  # Scroll to the bottom
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    user_list = [
        {"user_name": "User1", "lastest_message": "Hello, User1!", "avatar_image": "img.png"},
        {"user_name": "User2", "lastest_message": "Hello, User2!", "avatar_image": "img.png"},
        {"user_name": "User3", "lastest_message": "Hello, User3!", "avatar_image": "img.png"},
        {"user_name": "User4", "lastest_message": "Hello, User4!", "avatar_image": "img.png"},
        {"user_name": "User5", "lastest_message": "Hello, User5!", "avatar_image": "img.png"},
    ]
    chat_window = ChatWindow(user_list)
    chat_window.run()