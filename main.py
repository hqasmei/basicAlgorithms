# Author : Hosna Qasmei
# Created: 09/06/2020
# Description: Top 10 String manipulation algorithms with data integrity checks and logs

#!/usr/bin/python

from tkinter import *
from functools import partial
from basicAlgorithmsClass import reverse_integer, avg_words_len, add_int, unique_char, valid_palindrome, mono_arr, move_zeros, fill_blanks, matched_mismatched, prime_num_arr

class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title('Basic Algorithms Program - Version 1.0')
		master.geometry("740x500")

		self.label = Label(master, text='Welcome!')
		self.label.grid(row = 0, column = 0)

		self.border = Label(master, text='===================')
		self.border.grid(row = 1, column = 0)

        # ===================================================================================================
		self.label1  = LabelFrame(master, text='Reverse An Integer')
		self.entry1  = Entry(self.label1, width = 33)
		self.button1 = Button(self.label1, text="Enter", command=partial(self.reverse_integer_print,master))
		self.entry1.pack(side = 'left')
		self.button1.pack(side = 'right')
		self.label1.grid(row = 2, column = 0, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label2  = LabelFrame(master, text='Average Words Length')
		self.entry2  = Entry(self.label2, width = 33)
		self.button2 = Button(self.label2, text="Enter", command=partial(self.avg_words_len_print,master))
		self.entry2.pack(side = 'left')
		self.button2.pack(side = 'right')
		self.label2.grid(row = 2, column = 11, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label3  = LabelFrame(master, text='Add Two Integers')
		self.entry3  = Entry(self.label3, width = 16)
		self.entry4  = Entry(self.label3, width = 16)
		self.button3 = Button(self.label3, text="Enter", command=partial(self.add_int_print,master))
		self.entry3.pack(side = 'left')
		self.button3.pack(side = 'right')
		self.entry4.pack(side = 'left')
		self.label3.grid(row = 4, column = 0, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label5  = LabelFrame(master, text='First Unique Character')
		self.entry5  = Entry(self.label5, width = 33)
		self.button5 = Button(self.label5, text="Enter", command=partial(self.unique_char_print,master))
		self.entry5.pack(side = 'left')
		self.button5.pack(side = 'right')
		self.label5.grid(row = 4, column = 11, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label6  = LabelFrame(master, text='Valid Palindrome')
		self.entry6  = Entry(self.label6, width = 33)
		self.button6 = Button(self.label6, text="Enter", command=partial(self.valid_palindrome_print,master))
		self.entry6.pack(side = 'left')
		self.button6.pack(side = 'right')
		self.label6.grid(row = 6, column = 0, columnspan = 10, padx = 10, pady = 10)

		# # ===================================================================================================
		self.label7  = LabelFrame(master, text='Monotonic Array')
		self.entry7  = Entry(self.label7, width = 33)
		self.button7 = Button(self.label7, text="Enter", command=partial(self.mono_arr_print,master))
		self.entry7.pack(side = 'left')
		self.button7.pack(side = 'right')
		self.label7.grid(row = 6, column = 11, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label8  = LabelFrame(master, text='Move Zeroes')
		self.entry8  = Entry(self.label8, width = 33)
		self.button8 = Button(self.label8, text="Enter", command=partial(self.move_zeros_print,master))
		self.entry8.pack(side = 'left')
		self.button8.pack(side = 'right')
		self.label8.grid(row = 8, column = 0, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label9  = LabelFrame(master, text='Fill in the Blanks')
		self.entry9  = Entry(self.label9, width = 33)
		self.button9 = Button(self.label9, text="Enter", command=partial(self.fill_blanks_print,master))
		self.entry9.pack(side = 'left')
		self.button9.pack(side = 'right')
		self.label9.grid(row = 8, column = 11, columnspan = 10, padx = 10, pady = 10)


		# ===================================================================================================
		self.label10  = LabelFrame(master, text='Matched & Mismatched Words')
		self.entry10  = Entry(self.label10, width = 16)
		self.entry11  = Entry(self.label10, width = 16)
		self.button10 = Button(self.label10, text="Enter", command=partial(self.matched_mismatched_print,master))
		self.entry10.pack(side = 'left')
		self.button10.pack(side = 'right')
		self.entry11.pack(side = 'left')
		self.label10.grid(row = 10, column = 0, columnspan = 10, padx = 10, pady = 10)

		# ===================================================================================================
		self.label12  = LabelFrame(master, text='Prime Number Array')
		self.entry12  = Entry(self.label12, width = 33)
		self.button12 = Button(self.label12, text="Enter", command=partial(self.prime_num_arr_print,master))
		self.entry12.pack(side = 'left')
		self.button12.pack(side = 'right')
		self.label12.grid(row = 10, column = 11, columnspan = 10, padx = 10, pady = 10)



	def reverse_integer_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = reverse_integer(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)

	def avg_words_len_print(self,master):
		inputVal  = self.entry2.get()
		outputVal = avg_words_len(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 11, sticky='w', padx = 10, pady = 5)

	def add_int_print(self,master):
		inputVal1  = self.entry3.get()
		inputVal2  = self.entry4.get()
		outputVal  = add_int(inputVal1,inputVal2)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 5, column = 0, sticky='w', padx = 10, pady = 5)

	def unique_char_print(self,master):
		inputVal  = self.entry5.get()
		outputVal = unique_char(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 5, column = 11, sticky='w', padx = 10, pady = 5)


	def valid_palindrome_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = valid_palindrome(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal  = self.entry6.get()
		outputVal = valid_palindrome(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 7, column = 0, sticky='w', padx = 10, pady = 5)


	def mono_arr_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = mono_arr(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal  = list(self.entry7.get())
		outputVal = mono_arr(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 7, column = 11, sticky='w', padx = 10, pady = 5)


	def move_zeros_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = move_zeros(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal  = list(self.entry8.get())
		outputVal = move_zeros(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 9, column = 0, sticky='w', padx = 10, pady = 5)


	def fill_blanks_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = fill_blanks(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal  = list(self.entry9.get())
		outputVal = fill_blanks(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 9, column = 11, sticky='w', padx = 10, pady = 5)


	def matched_mismatched_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = matched_mismatched(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal1  = self.entry10.get()
		inputVal2  = self.entry11.get()
		print(inputVal1,inputVal2)
		outputVal = matched_mismatched(inputVal1, inputVal2)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 11, column = 0, sticky='w', padx = 10, pady = 5)


	def prime_num_arr_print(self,master):
		inputVal  = self.entry1.get()
		outputVal = prime_num_arr(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 3, column = 0, sticky='w', padx = 10, pady = 5)
		inputVal  = self.entry12.get()
		outputVal = prime_num-arr(inputVal)

		self.label = Label(master, text='Output: '+str(outputVal))
		self.label.grid(row = 11, column = 11, sticky='w', padx = 10, pady = 5)


if __name__ == "__main__":
	root = Tk()
	my_gui = MyFirstGUI(root)
	root.mainloop()
