import tkinter as tk
from tkinter import ttk

class HomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Match Tracker")
        self.root.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self.root, text="Football Match Tracker", font=("Arial", 16))
        title.pack(pady=20)

        # List of buttons to other windows
        buttons_info = [
            ("Register", self.open_register),
            ("Add / Update Matches", self.open_matches),
            ("Add / Update Players", self.open_players),
            ("Add / Update Teams", self.open_teams),
            ("Show Matches", self.open_show_matches),
            ("Show Teams", self.open_show_teams),
            ("Show Players", self.open_show_players),
            ("Show History Matches", self.open_history),
            ("Show Table Scoreboard", self.open_scoreboard),
            ("Statistics", self.open_statistics),
            ("Show Cards for Players", self.open_cards),
        ]

        for text, command in buttons_info:
            btn = ttk.Button(self.root, text=text, command=command)
            btn.pack(pady=5, fill='x', padx=50)

    def open_register(self):
        print("Open Register Window")

    def open_matches(self):
        print("Open Add/Update Matches Window")

    def open_players(self):
        print("Open Add/Update Players Window")

    def open_teams(self):
        print("Open Add/Update Teams Window")

    def open_show_matches(self):
        print("Open Show Matches Window")

    def open_show_teams(self):
        print("Open Show Teams Window")

    def open_show_players(self):
        print("Open Show Players Window")

    def open_history(self):
        print("Open History Matches Window")

    def open_scoreboard(self):
        print("Open Scoreboard Window")

    def open_statistics(self):
        print("Open Statistics Window")

    def open_cards(self):
        print("Open Cards for Players Window")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeGUI(root)
    root.mainloop()
