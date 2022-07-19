from abc import ABCMeta, abstractmethod


class Invoker(metaclass=ABCMeta):
	def toto(self):
		pass

class ICommand(metaclass=ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(self):
		pass

	@staticmethod
	@abstractmethod
	def unexecute(self):
			pass
	pass

class Command1(ICommand):
	def execute(self):
		pass

	def unexecute(self):
			pass
	pass

class Reciver:

	def task1(self):
		print('Running task1')

	def task2(self):
		print('Running task2')
	pass

class Remote:
	pass