import tkinter as tk
from tkinter import ttk, messagebox
from models.playermanager import PlayerManager

class ShowPlayersClass:
    def __init__(self, master):
        self.master = master
        self.master.title("Players List")
        self.master.geometry("700x400")

        self.player_manager = PlayerManager()

        title = tk.Label(master, text="All Players", font=("Arial", 16))
        title.pack(pady=10)

        columns = ("ID", "Name", "Team", "Position")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        refresh_btn = tk.Button(master, text="Refresh", command=self.load_players)
        refresh_btn.pack(pady=10)

        self.load_players()

    def load_players(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        players = self.player_manager.get_all_players()
        if not players:
            messagebox.showinfo("Info", "No players found or DB connection failed.")
            return

        for player_id, name, team, position in players:
            self.tree.insert("", tk.END, values=(player_id, name, team, position))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowPlayersClass(root)
    root.mainloop()

