class Human:
	def __init__(self, name, age, surname) -> None:
		self.name = name
		self.age = age
		self.surname = surname

	def __str__(self) -> str:
		return f"{self.name} {self.surname}, {self.age} years old"
	
	def __eq__(self, other) -> bool:
		return self.name == other.name and self.surname == other.surname and self.age == other.age

class Max(Human):	
	def getname(self):
		return self.name
	
	def getage(self):
		return self.age

	def getsurname(self):
		return self.surname


print(Max("John", 30, "Smith") == Human("John", 30, "Smith"))