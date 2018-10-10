#coding: utf-8

import simplePy.simplePy as simple

class simpleString():
	def __init__(self, v_simplePy, content = ""):
		if v_simplePy == simple.simplePy():
			self._content = content

	def __str__(self):
		return self._content

	def taille(self):
		return len(str(self._content))

	def est_vide(self):
		return self.taille() == 0

	def get_content(self):
		return self._content

	def set_content(self, value):
		self._content = value

	content = property(fget=get_content, fset=set_content)

	def append(self, value, to_begin = False):
		if to_begin:
			self._content = value + self._content
		else:
			self._content = self._content + value

	def at_index(self, index):
		if index < self.taille():
			return self._content[index]

	@staticmethod
	def open_parentheses(parenthese):
		if parenthese == ')':
			return '('
		elif parenthese == ']':
			return '['
		elif parenthese == '}':
			return '{'

	def check_parentheses(self):
		pile = []
		for char in self._content:
			if char == '(' or char == '[' or char == '{':
				pile.append(char)
			elif char == ')' or char == ']' or char == '}':
				if len(pile) == 0:
					return False
				elif pile[-1] == self.open_parentheses(char):
					pile.pop()
				else:
					return False
			else:
				pass
		return len(pile) == 0

	def sub_string_begin(self, begin):
		if begin >= 0:
			return str(self._content)[begin:]

	def sub_string_end(self, end):
		if end < self.taille():
			return str(self._content)[:-end]

	def sub_string_(self, begin, end):
		if begin >= 0 and end < self.taille():
			return str(self._content)[begin:-end]

	def center(self, len, char=" "):
		if len > (self.taille() + 1):
			taille = (len - self.taille()) // 2
			string = char*taille + self._content + char*taille
			return string

	def to_upper(self):
		return str.upper(str(self._content))

	def to_lower(self):
		return str.lower(str(self._content))

	def to_upfirst(self):
		return str.capitalize(str(self._content))