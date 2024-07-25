import tkinter as tk
from tkinter import filedialog
import time
from tkinter.font import Font

class ReadingSpeedTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reading Speed Trainer by Bjorka v1.3 ")
        self.root.resizable(False, False)  # Make the window fixed size

        # Create a menu frame at the top
        self.menu_frame = tk.Frame(root, bg='white')
        self.menu_frame.pack(side='top', fill='x')

        self.load_button = tk.Button(self.menu_frame, text="Load Text File", command=self.load_file, font=("Helvetica", 12), bg='white', fg='black')
        self.load_button.pack(side='left', padx=10, pady=5)

        self.speed_var = tk.StringVar(value="Standard")
        self.speed_options = {"Standard": 100, "Fast": 70, "Very fast": 30}
        self.speed_menu = tk.OptionMenu(self.menu_frame, self.speed_var, *self.speed_options.keys())
        self.speed_menu.config(font=("Helvetica", 12), bg='white', fg='black', activebackground='white', activeforeground='black')
        self.speed_menu["menu"].config(font=("Helvetica", 12), bg='white', fg='black')
        self.speed_menu.pack(side='left', padx=10, pady=5)

        self.start_button = tk.Button(self.menu_frame, text="Start", command=self.start, font=("Helvetica", 12), bg='white', fg='black')
        self.start_button.pack(side='left', padx=10, pady=5)

        self.stop_button = tk.Button(self.menu_frame, text="Stop", command=self.stop, font=("Helvetica", 12), bg='white', fg='black')
        self.stop_button.pack(side='left', padx=10, pady=5)

        self.canvas = tk.Canvas(root, bg='black', height=500, width=800)
        self.canvas.pack(expand=1, fill='both')

        self.font = Font(family="Helvetica", size=16)
        self.text_lines = []
        self.current_y = 500
        self.line_height = self.font.metrics("linespace")
        self.highlight_index = -1
        self.reading_start_time = None
        self.mid_point = 250  # Half of the canvas height
        self.running = False

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_lines = self.wrap_text(text)
            self.canvas.delete("all")
            self.current_y = 500
            self.highlight_index = -1

    def start(self):
        if self.text_lines:
            self.running = True
            self.reading_start_time = time.time()
            self.animate_text()

    def stop(self):
        self.running = False

    def wrap_text(self, text):
        wrapped_lines = []
        max_width = self.canvas.winfo_width() - 40  # 20 pixels padding on each side
        for line in text.split('\n'):
            while self.font.measure(line) > max_width:
                cut_index = 1
                while self.font.measure(line[:cut_index]) < max_width:
                    cut_index += 1
                space_index = line.rfind(' ', 0, cut_index)
                if space_index == -1:
                    space_index = cut_index
                wrapped_lines.append(line[:space_index])
                line = line[space_index:].strip()
            wrapped_lines.append(line)
        return wrapped_lines

    def animate_text(self):
        if not self.running:
            return

        self.canvas.delete("all")
        y_position = self.current_y

        for i in range(len(self.text_lines)):
            color = "white" if i == self.highlight_index else "grey"
            self.canvas.create_text(20, y_position, text=self.text_lines[i], font=self.font, fill=color, anchor="nw")
            y_position += self.line_height

        self.current_y -= 1

        if self.current_y < -self.line_height * len(self.text_lines):
            reading_end_time = time.time()
            total_time = reading_end_time - self.reading_start_time
            total_words = sum(len(line.split()) for line in self.text_lines)
            lines_per_minute = (len(self.text_lines) / total_time) * 60
            words_per_minute = (total_words / total_time) * 60
            result_message = f"Reading Speed:\nLines per minute: {lines_per_minute:.2f}\nWords per minute: {words_per_minute:.2f}"
            self.canvas.delete("all")
            self.canvas.create_text(400, 250, text=result_message, font=self.font, fill="white", anchor="center")
        else:
            if self.current_y <= self.mid_point:
                if self.highlight_index == -1:
                    self.highlight_index = 0
                elif self.current_y % self.line_height == 0:
                    self.highlight_index += 1

            speed = self.speed_options[self.speed_var.get()]
            self.root.after(speed, self.animate_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReadingSpeedTrainer(root)
    root.mainloop()
