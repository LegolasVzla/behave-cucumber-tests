#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

class Calculator:
	def __init__(self, number1, number2):
		self.number1 = int(number1)
		self.number2 = int(number2)

	def add(self):
		print(self.number1 + self.number2)
		return self.number1 + self.number2

	def subtract(self):
		print(self.number1 - self.number2)
		return self.number1 - self.number2

	def multiply(self):
		print(self.number1 * self.number2)
		return self.number1 * self.number2

	def divide(self):
		assert self.number2 > 0,"No soy tan inteligente como para dividir entre 0"
		print(self.number1 / self.number2)			
		return self.number1 / self.number2

	def execute(self,operation):
		if operation == 'sumar':
			return self.add()
		if operation == 'restar':
			return self.subtract()
		if operation == 'multiplicar':
			return self.multiply()
		if operation == 'dividir':
			return self.divide()
		else:
			print("Invalid operation")

if __name__ == "__main__":
	operation = sys.argv[1]
	number1 = sys.argv[2]
	number2 = sys.argv[3]
	calculator = Calculator(number1,number2)
	calculator.execute(operation)
