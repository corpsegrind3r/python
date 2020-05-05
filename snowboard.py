# Snowboard class

class Snowboard:
	"""My snowboard class"""

	def __init__(self,make,model,length): # 
		self.make = make # variables that are accessible through instances are called attributes
		self.model = model
		self.length = length
		self.days_used = days_used = 0

	def details(self): # a function that is part of a class is called a method
		print(f"This snowboard is a {self.make} {self.model} {self.length} and has been used for {self.days_used} days.")

	def increment_days_used(self,days):
		if days > 0:
			self.days_used += days
		else: 
			print("You cannot remove days used!")



first_snowboard = Snowboard('Burton','Custom',152)
second_snowboard = Snowboard('K2','Praying Mantis',158)

second_snowboard.increment_days_used(4)

first_snowboard.details()
second_snowboard.details()