import json

class Model:
	def __init__(self, class_ex):
		self.class_ex=class_ex

	def save(self):
		ex=self.class_ex()
		keys=list(filter(lambda x: not x.startswith('_'), dir(self.class_ex)))
		All_argument={}
		for i in keys:
			command="ex."+str(i)
			All_argument[i]=eval(command)
		name=str(self.class_ex)
		name=name.replace("<class '__main__.",'').replace("'>",'')
		name+=".json"
		with open(name,'w',encoding='utf-8') as f:
			json.dump(All_argument,f)
		

class C2:
 	title = '1'
 	text = '2'
 	author = '3'
 	example='smth'


example=Model(C2)
example.save()

