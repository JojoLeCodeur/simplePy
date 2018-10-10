#coding: utf-8

class simplePy:
	def __init__(self):
		self._simplePyActivated = True

	@property
	def simplePyActivated(self):
		return self._simplePyActivated

	@simplePyActivated.setter
	def simplePyActivated(self, value):
		if value == True or value == False:
			self._simplePyActivated = value
		else:
			raise TypeError("value must be (bool) True or (bool) False")

	def __eq__(self, obj):
		if hasattr(obj, "simplePyActivated"):
			return self._simplePyActivated == obj.simplePyActivated
		else:
			return False