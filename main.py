# Author : Hosna Qasmei
# Created: 09/06/2020
# Description: Top 10 String manipulation algorithms with data integrity checks and logs

#!/usr/bin/python

from tkinter import *
from functools import partial
from basicAlgorithmsClass import reverse_integer, avg_words_len

class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title('Basic Algorithms Program - Version 1.0')
		master.geometry("500x200")

		self.label = Label(master, text='Welcome!')
		self.label.grid(row = 0, column = 1)

		self.border = Label(master, text='=============================')
		self.border.grid(row = 1, column = 1)

        # ===================================================================================================
		self.label1 = Label(master, text='Reverse Integer')
		self.label1.grid(row = 2, column = 1)

		self.entry1 = Entry(master)
		self.entry1.grid(row = 3, column = 1)

		self.button1 = Button(master, text="Enter", command=partial(self.reverse_integer_print,master))
		self.button1.grid(row = 3, column = 2)

		self.border1 = Label(master, text='=============================')
		self.border1.grid(row = 5, column = 1)

		# ===================================================================================================
		self.label2 = Label(master, text='Average Words Length')
		self.label2.grid(row = 6, column = 1)

		self.entry2 = Entry(master)
		self.entry2.grid(row = 7, column = 1)

		self.button2 = Button(master, text="Enter", command=partial(self.avg_word_len_print,master))
		self.button2.grid(row = 7, column = 2)

		self.border2 = Label(master, text='=============================')
		self.border2.grid(row = 9, column = 1)




	def reverse_integer_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = reverse_integer(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 4, column = 1)


	def avg_word_len_print(self,master):
		inputVal  = self.entry2.get()
		outputVal = avg_words_len(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 8, column = 1)	



if __name__ == "__main__":
	root = Tk()
	my_gui = MyFirstGUI(root)
	root.mainloop()