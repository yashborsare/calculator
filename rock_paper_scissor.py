import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import pygame
from pygame.locals import *



class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("600x500")
        self.root.configure(bg='#2E0854')

        self.user_score = 0
        self.computer_score = 0
        

        self.label = tk.Label(root, text="Choose Your Option", font="arial 20 bold", fg='#ffffff', bg='#2E0854')
        self.label.pack(pady=30)

        self.buttons_frame = tk.Frame(root, bg='#2E0854')
        self.buttons_frame.pack()

        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            button = tk.Button(self.buttons_frame, text=choice, font="arial 20 bold", fg='#ffffff', bg='#fa05e1', padx=20, pady=10, command=lambda ch=choice: self.play_game(ch))
            button.pack(side=tk.LEFT, padx=5)

        pygame.init()

    def play_game(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.show_scores()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "You lose!"

    def show_scores(self):
        score_text = f"User Score: {self.user_score}  |  Computer Score: {self.computer_score}"
        self.score_label = tk.Label(self.root, text=score_text, font=("arial 15 bold"), fg='#05e1fa', bg='#2E0854')
        self.score_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    
#icon
Image_icon=PhotoImage(file="F:/Icons/game.png")
root.iconphoto(False,Image_icon)

root.mainloop()
