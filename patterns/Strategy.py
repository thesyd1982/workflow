import types


class Strategy:
	def __init__(self, function=None):
		self.name = 'Default Strategy'
		# If a reference to a function is provided , repalace execute method by function
		if function:
			self.execute = types.MethodType(function, self)

	def execute(self):
		print(f'{self.name} is used!')
	pass


pass


# Replacment method 1
def strategy_one(self):
	print(f'{self.name} is used to execute method 1')


# Replacment method 2
def strategy_two(self):
	print(f'{self.name} is used to execute method 2')


s0 = Strategy()
s0.execute()

s1 = Strategy(function=strategy_one)
s1.name = 'Strat One'
s1.execute()


s2 = Strategy(function=strategy_two)
s2.name = 'Strat Two'
s2.execute()

