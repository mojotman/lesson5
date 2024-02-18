class Point():
	def __init__(self, x,y):
		self.x=float(x)
		self.y=float(y)
	def vector(self):
		return (self.x**2+self.y**2)**(1/2)
	def get(self):
		return [self.x, self.y]
	def __add__(self,other):
		newx=self.x+other.x
		newy=self.y+other.y
		return Point(newx,newy)
	def __sub__(self,other):
		newx=self.x-other.x
		newy=self.y-other.y
		return Point(newx,newy)
	def __mul__(self,other):
		if type(other)==int or type(other)==float:
			newx=self.x*other
			newy=self.y*other
			return Point(newx,newy)
		else:
			scalar=self.x*other.x+self.y*other.y
			return scalar
	def distant(self,other):
		return ((other.x-self.x)**2+(other.y-self.y)**2)**(1/2)

a=Point(1,1)
b=Point(2,5)


print("вектор a: " +str(a.get()) )
print("вектор b: " +str(b.get()) )
print("длина вектора a: " + str(a.vector()))
a2=a*2
print("умножим а на 2: "+str(a2.get()))
print("произведение векторов а и b: "+str(a*b))
c1=a+b
print("сложене векторов а и b: " +str(c1.get()))
c2=b-a
print("вычитание вектора а из b: " +str(c2.get()))
print("расстояние между точками а и b: " + str(a.distant(b)))