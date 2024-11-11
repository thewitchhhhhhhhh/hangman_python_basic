import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x600")
        self.root.configure(bg='black')

        # Start Page
        self.start_frame = tk.Frame(root, bg='black')
        self.start_frame.pack(fill='both', expand=True)

        self.start_label = tk.Label(self.start_frame, text="Hangman Game", font=('Ariel', 32, 'bold'), fg='white', bg='black')
        self.start_label.pack(pady=50)

        self.developer_label = tk.Label(self.start_frame, text="Developer: Rimsha Shaikh", font=('Ariel', 16), fg='white', bg='black')
        self.developer_label.pack(pady=20)

        self.start_button = tk.Button(self.start_frame, text="Start Game", font=('Ariel', 16), fg='white', bg='#006400', command=self.show_game_screen)
        self.start_button.pack(pady=20)

        # Game Page
        self.game_frame = tk.Frame(root, bg='black')

        # Game variables
        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.reset_game()

        # Title label
        self.title_label = tk.Label(self.game_frame, text="Hangman Game", font=('Ariel', 24, 'bold'), fg='white', bg='black')
        self.title_label.pack(pady=20)

        # Canvas for drawing hangman
        self.canvas = tk.Canvas(self.game_frame, width=200, height=200, bg='black', highlightthickness=0)
        self.canvas.pack(pady=20)
        self.draw_base()

        # Word display
        self.word_display = tk.Label(self.game_frame, text=self.get_display_word(), font=('Ariel', 18), fg='white', bg='black')
        self.word_display.pack(pady=20)

        # Lives display
        self.lives_label = tk.Label(self.game_frame, text=f"Lives: {self.lives}", font=('Ariel', 16), fg='white', bg='black')
        self.lives_label.pack(pady=10)

        # Entry for guesses
        self.guess_entry = tk.Entry(self.game_frame, font=('Ariel', 16), fg='black', bg='white')
        self.guess_entry.pack(pady=10)

        # Guess button
        self.guess_button = tk.Button(self.game_frame, text="Guess", font=('Ariel', 16), fg='white', bg='#006400', command=self.make_guess)
        self.guess_button.pack(pady=10)

        # Result message
        self.result_label = tk.Label(self.game_frame, text="", font=('Ariel', 16), fg='white', bg='black')
        self.result_label.pack(pady=20)

        # Play Again button
        self.play_again_button = tk.Button(self.game_frame, text="Play Again", font=('Ariel', 16), fg='white', bg='#006400', command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()

    def show_game_screen(self):
        self.start_frame.pack_forget()
        self.game_frame.pack(fill='both', expand=True)

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guesses = ""
        self.lives = 6
        if hasattr(self, 'canvas'):
            self.canvas.delete("all")
            self.draw_base()
        if hasattr(self, 'word_display'):
            self.word_display.config(text=self.get_display_word())
            self.lives_label.config(text=f"Lives: {self.lives}")
            self.result_label.config(text="")
        if hasattr(self, 'guess_button'):
            self.guess_button.config(state=tk.NORMAL)
            self.guess_entry.config(state=tk.NORMAL)
            self.play_again_button.pack_forget()

    def get_display_word(self):
        display_word = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        return ' '.join(display_word)

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guesses:
                self.result_label.config(text="You already guessed that letter.")
            elif guess in self.word:
                self.guesses += guess
                self.result_label.config(text="Good guess!")
            else:
                self.guesses += guess
                self.lives -= 1
                self.result_label.config(text="Wrong guess.")
                self.update_hangman()
            self.update_game_status()
        else:
            self.result_label.config(text="Please enter a single letter.")

    def update_game_status(self):
        self.word_display.config(text=self.get_display_word())
        self.lives_label.config(text=f"Lives: {self.lives}")

        if self.lives <= 0:
            self.result_label.config(text=f"You lost! The word was '{self.word}'.")
            self.end_game()
        elif '_' not in self.get_display_word():
            self.result_label.config(text="Congratulations! You guessed the word!")
            self.end_game()

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def draw_base(self):
        self.canvas.create_line(20, 180, 180, 180, fill='white', width=2)  # Base
        self.canvas.create_line(40, 20, 40, 180, fill='white', width=2)   # Pole
        self.canvas.create_line(40, 20, 140, 20, fill='white', width=2)   # Top bar
        self.canvas.create_line(140, 20, 140, 40, fill='white', width=2)  # Rope

    def update_hangman(self):
        if self.lives == 5:
            self.canvas.create_oval(120, 40, 160, 80, outline='white', width=2)  # Head
        elif self.lives == 4:
            self.canvas.create_line(140, 80, 140, 140, fill='white', width=2)   # Body
        elif self.lives == 3:
            self.canvas.create_line(140, 100, 120, 120, fill='white', width=2)  # Left arm
        elif self.lives == 2:
            self.canvas.create_line(140, 100, 160, 120, fill='white', width=2)  # Right arm
        elif self.lives == 1:
            self.canvas.create_line(140, 140, 120, 160, fill='white', width=2)  # Left leg
        elif self.lives == 0:
            self.canvas.create_line(140, 140, 160, 160, fill='white', width=2)  # Right leg

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
