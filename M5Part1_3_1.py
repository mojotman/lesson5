import random
class Voin():
	
	def __init__(self, hp,name):
		self.hp=float(hp)
		self.name=name
	def battle(self,other):
		while self.hp>0 and other.hp>0:
			r=random.randint(0,1)
			if r>0.5:
				other.hp-=20
				print("воин "+str(self.name)+ " атаковал и оставил у противника " + str(other.hp) + "HP")
			else:
				self.hp-=20
				print("воин "+str(other.name)+ " атаковал и оставил у противника " + str(self.hp) + "HP")
			if self.hp<=0:
				print("воин "+str(other.name)+" победил")
				return
			elif other.hp<=0:
				print("воин "+str(self.name)+" победил")
				return


v1=Voin(100,"кот Борис")
v2=Voin(100,"Бэтмен")
v1.battle(v2)
