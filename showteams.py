import sys
print(sys.path)
import tkinter as tk
from tkinter import messagebox
from models.teammanager import TeamManager

class ShowTeams:
    def __init__(self, root):
        self.manager = TeamManager()

        root.title("Teams List")
        root.geometry("300x400")

        self.listbox = tk.Listbox(root, width=40, height=20)
        self.listbox.pack(pady=20)

        tk.Button(root, text="Refresh", command=self.show_teams).pack(pady=5)
        self.show_teams()

    def show_teams(self):
        self.listbox.delete(0, tk.END)
        teams = self.manager.fetch_teams()

        if not teams:
            messagebox.showinfo("Info", "No teams found or failed to load.")
            return

        for team_id, team_name in teams:
            self.listbox.insert(tk.END, f"{team_name} (ID: {team_id})")

if __name__ == "__main__":
    root = tk.Tk()
    ShowTeams(root)
    root.mainloop()

