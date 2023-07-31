"""
    Entry point for application
"""

import os
import sys
import random
import customtkinter
from tkinter import BitmapImage
from games import Games

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # ICON
        try:
            from ctypes import windll
            myappid = "mycompany.myproduct.subproduct.version"
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError:
            pass

        self.iconbitmap(self.resource_path("icon.ico"))

        # Config window
        self.title("Jackbox games")
        self.geometry("500x300")

        # Create input
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,2), weight=1)

        # Player entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Number of Players")
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="")

        # Button
        self.button = customtkinter.CTkButton(self, text="Choose game", command=self.show_game)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="")

        # Output
        self.output = customtkinter.CTkLabel(self, text=" NONE ")
        self.output.grid(row=2, column=0, padx=10, pady=10, sticky="")

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def show_game(self):
        """Button logic"""
        try:
            numPlayers = int(self.entry.get())
        except ValueError:
            self.output.configure(text="INVALID INPUT")
        
        if numPlayers > 10:
            raise Exception(self.output.configure(text="INVALID INPUT"))

        game = self.ChooseGame(numPlayers)
        game_name = game[0] + " " + "(" + game[3] + ")"
        self.output.configure(text=f"{game_name}")


    def ChooseGame(self, numPlayers, *drawing):
        """Game picker logic, returns (name, min numPlayer, max numPlayer, pack number, isDrawing)"""
        game_list = []
        even_players = False

        if int(numPlayers) % 2 == 0:
            even_players = True

        for game in Games:
            if(int(numPlayers) >= game[1] and int(numPlayers) <= game[2]):
                if even_players == False and game[0] == "Quixort":
                    continue
                elif even_players == False and game[0] == "Poll mine":
                    continue
                else:
                    game_list.append(game)

        return game_list[random.randint(0, len(game_list) - 1)]


if __name__ == "__main__":
    app = App()
    app.mainloop()
    