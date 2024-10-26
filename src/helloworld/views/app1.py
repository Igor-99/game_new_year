

class Mammals():
	def to_eat():
		print("im to_eat")
	def run():
		print("Бег")
	def fly():
		print("летать")

class Cat():
	def muay():
		print("мяу")
class Owl():
	
	def fly():
		mammals = Mammals.fly()
		# return mammals
	def ururu():
		print("Уруру")
class World():
	def __init__(self, obj):
		print(obj)
world = World(Owl.fly())
def main():

    return World()