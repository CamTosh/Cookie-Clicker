# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk
from PIL import Image
import sqlite3


class Interface(Frame):

	
	def __init__(self, fenetre, conn, **kwargs):

		self.conn = conn
		self.u = User(self.conn)

		self.store = {'Double clics': 100,
					  'Mamie': 1000,
					  'Space Cookie': 424242,
					  'Double Mamie': 69696969,
					  'Cookie Psyche': 6942694269}

		Frame.__init__(self, fenetre, **kwargs)
		self.pack(fill=BOTH)

		self.photo = ImageTk.PhotoImage(file="cookie.png")
		self.cookie = Canvas(fenetre, width = 640, height = 392)
		self.cookie.focus_set()
		self.cookie.create_image(0, 0, anchor = NW, image=self.photo)
		self.cookie.bind('<Button-1>', self.cliquer)
		self.cookie.pack()

		self.v = StringVar()
		self.v.set("Tu as "+ str(self.result()) +" cookie(s)")
		self.message = Label(self, textvariable=self.v)
		self.message.pack()

		self.liste()

		
	def result(self):

		self.conn.row_factory = sqlite3.Row

		for row in self.conn.execute("SELECT points FROM user"):
			pts = row["points"]

		self.conn.close

		return pts

	
	def cliquer(self, event):

		c = self.u.clic()
		self.v.set("Tu as " + str(self.result()) + " cookies")

	
	def liste(self):

		listbox = Listbox(fenetre)
		listbox.pack()

		for k, v in sorted(self.store.items(), key = lambda kv: kv[1], reverse=False):

			listbox.insert(END, k + " " + str(v))
			listbox.config(width = len(k + str(v)) + 1, height = len(self.store.items()))


class User(object):

	
	def __init__(self, conn):

		self.nb_clic = self.result()
		self.conn = conn

	
	def clic(self):

		self.nb_clic += 1
		print(self.nb_clic)
		chaine = "UPDATE user set points = " + str(self.nb_clic)
		self.conn.execute(chaine)
		self.conn.commit()
		self.conn.close

		return self.nb_clic


	def result(self):

		conn.row_factory = sqlite3.Row
		for row in conn.execute("SELECT points FROM user"):

			pts = row["points"]
		return pts


if __name__ == '__main__':

	conn = sqlite3.connect('game.db')
	fenetre = Tk()
	interface = Interface(fenetre, conn)
	fenetre['bg'] = 'white'

	interface.mainloop()
	# interface.destroy()
