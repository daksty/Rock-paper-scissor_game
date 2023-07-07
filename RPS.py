import tkinter as tk
import random
from PIL import ImageTk,Image
import time


w = tk.Tk()
score = 0
escore = 0
choosed = "none"

def choices():
	def backt():
		rockb.config(bg = "white")
		paperb.config(bg = "white")
		scissorb.config(bg = "white")
		enrock.config(bg = "white")
		enpaper.config(bg = "white")
		enscissor.config(bg = "white")
		ress.config(text = "Result: ", bg = "white")
		
	def chplay():
		global score
		global escore
		global choosed
		if choosed == "rock":
			rockb.config(bg = "green")
			paperb.config(bg = "red")
			scissorb.config(bg = "red")
			rockq = ["rock","paper","scissor"]
			rocc = random.choice(rockq)
			if rocc == "rock":
				enrock.config(bg = "green")
				enpaper.config(bg = "red")
				enscissor.config(bg = "red")
				ress.config(text = "Result: Tie", bg = "yellow")
				w.after(1000, backt)
			elif rocc == "paper":
				enrock.config(bg = "red")
				enpaper.config(bg = "green")
				enscissor.config(bg = "red")
				ress.config(text = "Result: Lose", bg = "red")
				escore += 1
				youre.config(text = "Opponent score: " + str(escore))
				w.after(1000,backt)
			elif rocc == "scissor":
				enrock.config(bg = "red")
				enpaper.config(bg = "red")
				enscissor.config(bg = "green")
				ress.config(text = "Result: You win", bg = "green")
				score += 1
				yours.config(text = "Your score: " + str(score))
				w.after(1000,backt)
		elif choosed == "paper":
				rockb.config(bg = "red")
				paperb.config(bg = "green")
				scissorb.config(bg = "red")
				paf = ["rock","paper","scissor"]
				pape = random.choice(paf)
				if pape == "rock":
					score += 1
					enrock.config(bg = "green")
					enpaper.config(bg = "red")
					enscissor.config(bg = "red")
					ress.config(text = "Result: You win", bg = "green")
					yours.config(text = "Your score: " + str(score))
					w.after(1000, backt)
				elif pape == "paper":
					enrock.config(bg = "red")
					enpaper.config(bg = "green")
					enscissor.config(bg = "red")
					ress.config(text = "Result: Tie",bg = "yellow")
					w.after(1000, backt)
				elif pape == "scissor":
					enrock.config(bg = "red")
					enpaper.config(bg = "red")
					enscissor.config(bg = "green")
					ress.config(text = "Result: You lose", bg = "red")
					escore += 1
					youre.config(text = "Opponent score: " + str(escore))
					w.after(1000,backt)
					
		elif choosed == "scissor":
				rockb.config(bg = "red")
				paperb.config(bg = "red")
				scissorb.config(bg = "green")
				sci = ["rock","paper","scissor"]
				gs = random.choice(sci)
				if gs == "rock":
					enrock.config(bg = "green")
					enpaper.config(bg = "red")
					enscissor.config(bg = "red")
					escore += 1
					youre.config(text = "Opponent score: "+ str(escore))
					ress.config(text = "Result: You lose", bg = "red")
					w.after(1000, backt)
				elif gs == "paper":
						enrock.config(bg = "red")
						enpaper.config(bg = "green")
						enscissor.config(bg = "red")
						score += 1
						ress.config(text = "Result: You win", bg = "green")
						yours.config(text = "Your score: "+ str(score))
						w.after(1000,backt)
				elif gs == "scissor":
						enrock.config(bg = "red")
						enpaper.config(bg = "red")
						enscissor.config(bg = "green")
						ress.config(text = "Result: Tie",bg = "yellow")
						w.after(1000,backt)
						
						
					
		
		
		
	def rch():
		global choosed
		choosed = "rock"
		chplay()
	def pch():
		global choosed
		choosed = "paper"
		chplay()
	def sch():
		global choosed
		choosed = "scissor"
		chplay()
	
	yours = tk.Label(w, text = "Your score: 0")
	yours.place(y = 200, x = 10)
	youre = tk.Label(w, text = "Opponent score: 0")
	youre.place(y = 980, x = 10)
	yourturn = tk.Label(w, text = "Your turn", font = ("pixel8",10,"bold"), relief = "sunken",bg = "yellow")
	yourturn.place(y = 240, x = 285)
	rock = Image.open("rock/rock.png")
	rocks = ImageTk.PhotoImage(rock)
	rockb = tk.Button(w, image = rocks, width = 150, height = 150, bg = "white", command = rch)
	rockb.place(y = 300, x = 120)
	ress = tk.Label(w, text = "Result: ",font = ("pixel8",10,"bold"))
	ress.place(y = 600, x = 250)
	paper = Image.open("rock/paper.png")
	papers = ImageTk.PhotoImage(paper)
	paperb = tk.Button(w, image = papers, width = 150, height = 150, bg = "white", command = pch)
	paperb.place(y = 300, x = 290)
	
	scissor = Image.open("rock/scissor.png")
	scissors = ImageTk.PhotoImage(scissor)
	scissorb = tk.Button(w, image = scissors,width = 150, height = 150, bg = "white", command = sch)
	scissorb.place(y = 300, x = 460)
	
	enrock = tk.Label(w, image = rocks, bg = "white", width = 150, height = 150, relief = "solid")
	enrock.place(y =800, x =110)
	enpaper = tk.Label(w, image = papers, width = 150, height = 150, relief = "solid", bg = "white")
	enpaper.place(y = 800, x = 280)
	enscissor = tk.Label(w, image = scissors,width = 150, height = 150, relief = "solid", bg = "white")
	enscissor.place(y = 800, x = 450)
	enturn = tk.Label(w, text = "Opponent turn", bg = "red",font = ("pixel8",10,"bold"),relief = "ridge")
	enturn.place(y = 735, x = 230)
	w.mainloop()

bg = Image.open("rock/backround.png")
bgr = bg.resize((900,1600))
bgs = ImageTk.PhotoImage(bgr)
bgsl = tk.Label(w, image = bgs)
bgsl.place(y =0, x = -90)
choices()

w.mainloop()