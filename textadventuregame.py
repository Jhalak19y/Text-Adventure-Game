import tkinter as tk
from PIL import Image, ImageTk

class AdventureGameApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Adventure Game")
        self.window.geometry("600x500")

        # Load initial scene image and configure widgets
        self.load_images()
        self.configure_widgets()

    def load_images(self):
        # Load images and resize as needed
        self.img_intro = Image.open("cave entrance.jpg").resize((400, 300), Image.Resampling.LANCZOS)
        self.img_explore = Image.open("cave path.jpg").resize((400, 300), Image.Resampling.LANCZOS)
        self.img_left_path = Image.open("treasure.png").resize((400, 300), Image.Resampling.LANCZOS)
        self.img_straight_path = Image.open("artifact.jpg").resize((400, 300), Image.Resampling.LANCZOS)

        # Convert images to Tkinter PhotoImage objects
        self.img_intro_tk = ImageTk.PhotoImage(self.img_intro)
        self.img_explore_tk = ImageTk.PhotoImage(self.img_explore)
        self.img_left_path_tk = ImageTk.PhotoImage(self.img_left_path)
        self.img_straight_path_tk = ImageTk.PhotoImage(self.img_straight_path)

    def configure_widgets(self):
        # Initial scene widgets
        self.label_intro_image = tk.Label(self.window, image=self.img_intro_tk)
        self.label_intro_image.pack(pady=10)

        self.label_intro_text = tk.Label(self.window, text="You find yourself standing at the entrance of a dark cave.\nA mysterious voice echoes in your mind: 'Brave adventurer, who seeks the truth, enter if you dare.'")
        self.label_intro_text.pack(pady=10)

        self.button_enter = tk.Button(self.window, text="Enter the cave", command=self.explore_cave)
        self.button_enter.pack(pady=5)

        self.button_walk_away = tk.Button(self.window, text="Walk away", command=self.walk_away)
        self.button_walk_away.pack(pady=5)

        # Exploration scene widgets
        self.label_explore_image = tk.Label(self.window, image=self.img_explore_tk)
        self.label_explore_text = tk.Label(self.window, text="As you move deeper into the darkness, you see two paths ahead of you.\nOne path seems to lead to the left, and the other continues straight.")
        self.button_left_path = tk.Button(self.window, text="Take the left path", command=self.left_path)
        self.button_straight_path = tk.Button(self.window, text="Proceed straight ahead", command=self.straight_path)

        # Result scene widgets
        self.label_left_path_image = tk.Label(self.window, image=self.img_left_path_tk)
        self.label_result_text = tk.Label(self.window, text="Suddenly, you encounter a chest filled with gold coins!\nCongratulations! You have found the treasure.\nYou have completed your adventure.")

        self.label_straight_path_image = tk.Label(self.window, image=self.img_straight_path_tk)
        self.label_result_text_straight = tk.Label(self.window, text="You reach a dead end and discover an ancient artifact.\nYou take it with you as a memento of your journey.\nYou have completed your adventure.")

    def explore_cave(self):
        self.label_intro_image.pack_forget()
        self.label_intro_text.config(text="You cautiously step into the cave...")
        self.button_enter.config(state=tk.DISABLED)
        self.button_walk_away.config(state=tk.DISABLED)

        self.label_explore_image.pack(pady=10)
        self.label_explore_text.pack(pady=10)
        self.button_left_path.pack(pady=5)
        self.button_straight_path.pack(pady=5)

    def left_path(self):
        self.label_explore_image.pack_forget()
        self.label_explore_text.config(text="You choose the left path and walk for what feels like hours.")

        self.label_left_path_image.pack(pady=10)
        self.label_result_text.pack(pady=10)

        self.button_left_path.config(state=tk.DISABLED)
        self.button_straight_path.config(state=tk.DISABLED)

    def straight_path(self):
        self.label_explore_image.pack_forget()
        self.label_explore_text.config(text="You continue straight ahead, carefully navigating through narrow passages.")

        self.label_straight_path_image.pack(pady=10)
        self.label_result_text_straight.pack(pady=10)

        self.button_left_path.config(state=tk.DISABLED)
        self.button_straight_path.config(state=tk.DISABLED)

    def walk_away(self):
        self.label_intro_image.pack_forget()
        self.label_intro_text.config(text="You decide not to enter the cave and walk away.")

        self.label_walk_away_text = tk.Label(self.window, text="You return home safely, but always wonder what secrets the cave held.")
        self.label_walk_away_text.pack(pady=10)

        self.button_enter.config(state=tk.DISABLED)
        self.button_walk_away.config(state=tk.DISABLED)

def main():
    window = tk.Tk()
    app = AdventureGameApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
