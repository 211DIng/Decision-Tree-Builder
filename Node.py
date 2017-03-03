class Node:
	def __init__(self, data = ''):
		self.data = data
		self.children = []

	def is_empty(self):
		return (self.data is None)

	def set_data(self,data):
		self.data = data

	def get_data(self):
		return self.data

	def add_child(self, child):
		self.children.append(child)

	def get_children(self):
		return self.children
		
	def __repr__(self, level = 0):
		representation = "\t" * level + "|" + "-" * level + repr(self.data) + "\n"
		for child in self.children:
			representation += child.__repr__(level + 1)
		return representation

