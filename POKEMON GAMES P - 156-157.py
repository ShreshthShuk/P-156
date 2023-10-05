from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Pokemon Game")
root.geometry("500x500")
root.configure(background="yellow")

pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg")) 
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg")) 
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg")) 
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg")) 
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg")) 
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg")) 
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg")) 
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg")) 
persion = ImageTk.PhotoImage(Image.open("persion.jpg")) 
abra = ImageTk.PhotoImage(Image.open("abra.jpg")) 
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg")) 
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg")) 

player1 = Label(root, bg = "royal blue", fg = "white", text = "Player 1")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, bg = "royal blue", fg = "white", text = "Player 2")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player1_score = Label(root, bg = "royal blue", fg = "white")
player1_score.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2_score = Label(root, bg = "royal blue", fg = "white")
player2_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_game = Label(root, bg = "chocolate", fg = "white")
random_dice_game.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()