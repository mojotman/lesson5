class String_var():
	def __init__(self, strData):
		self.strData=str(strData)
	def set(self, newData):
		self.strData=str(newData)
	def get(self):
		return self.strData


example=String_var('строка 1')
print(example.get())
example.set("строка 2")
print(example.get())
example.set([1,2,3])
print(example.get())


