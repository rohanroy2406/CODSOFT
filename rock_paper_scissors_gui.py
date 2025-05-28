import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x350")
root.resizable(False, False)

# Global variables
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

# Functions
def get_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Scissors" and comp == "Paper") or \
         (user == "Paper" and comp == "Rock"):
        return "User"
    else:
        return "Computer"

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    winner = get_winner(user_choice, comp_choice)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {comp_choice}")

    if winner == "User":
        user_score += 1
        result_label.config(text=result_label.cget("text") + "\nYou win this round! 🎉")
    elif winner == "Computer":
        computer_score += 1
        result_label.config(text=result_label.cget("text") + "\nComputer wins this round! 🤖")
    else:
        result_label.config(text=result_label.cget("text") + "\nIt's a tie!")

    update_score()

def update_score():
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score → You: 0 | Computer: 0")
    result_label.config(text="Make your move!")

# GUI Layout
tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

root.mainloop()
