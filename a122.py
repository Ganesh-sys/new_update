# Define a rectangle class which has a method area() to return the area of a rectangle. 
#Define a square class which will leverage the rectangle class method area() to calculate its own area.
# # Find the area of a square with side length 4.

# class rectangle:
# 	def area(self):
# 		return l*b
# class square(rectangle):
# 	def area(self):
# 		return l*l

def decor(func):
	def inner(name):
		print("decorator execution")
		func(name)

	return inner

@decor
def wish(name):
	print("Hello",name,"Good Afternoon")

wish()



