from Tkinter import *
import random

class guessGame:

    def __init__(self, master):
        #create root window
        #root = Tk()
        frame = Frame(master)
        frame.pack()

        #Create Widgets
        self.label_title = Label(root, text="Welcome to the Guessing Game")
        self.label_title.pack()

        self.label_result = Label(root, text="Good Luck!")
        self.label_result.pack()

        self.button_check = Button(root, text="Check", fg="blue", command=self.check)
        self.button_check.pack()

        self.button_reset = Button(root, text="Play again", fg="purple", command=self.resetGame)
        self.button_reset.pack()

        self.button_quit = Button(root, text='Quit', fg= "red", command=quit)
        self.button_quit.pack()

        self.txt_guess = Entry(root, width=3)
        self.txt_guess.pack(side=BOTTOM)

        self.computer_guess = random.randint(1, 10)

        self.life = 4

    def resetGame(self):
        #self.computer_guess = random.randint(1, 10)
        self.computer_guess = random.randint(1, 10)
        #txt_guess.delete = delets the Entry box when user clocks on "Generate New Number"
        self.txt_guess.delete(0, 'end')
        self.label_result["text"] = "Please enter a number"

        self.life = 4

    def check(self):
        try:
            #Get the value from txt_guess, whatever value typed into user guess
            self.user_guess = int(self.txt_guess.get())

            #Determine higher, lower, or correct
            if self.user_guess < self.computer_guess:
                self.life -= 1
                self.msg = "Your guess is too low, you have %d life left" %self.life
                if self.life == 0:
                    self.msg= "You Loose, the number was %d!" %self.computer_guess
                    gen.resetGame()


            elif self.user_guess > self.computer_guess:
                if self.life == 0:
                    # self.label_result["text"] = "You Loose!"
                    self.msg = "You Loose, the number was %d" %self.computer_guess
                    gen.resetGame()
                self.life -= 1
                self.msg = "Your guess is too high, you have %d life left" %self.life
                # if self.life == 0:

            if self.user_guess == self.computer_guess:
                self.msg = "Correct!"

            #Show the result in the Tkinter grid
            self.label_result["text"] = self.msg

        except:
            self.label_result["text"] = "Please only input numbers"


#Start the main events loop
root = Tk()
gen = guessGame(root)
root.mainloop()
