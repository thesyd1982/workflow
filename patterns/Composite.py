from abc import ABC, abstractmethod


class Component(ABC):
	def __init__(self, *args, **kwargs):
		pass

	@abstractmethod
	def execute(self):
		pass


class Child(Component):
	def __init__(self, *args, **kwargs):
		Component.__init__(*args, **kwargs)
		self.parent = None
		self.name = args[0]

	def execute(self):
		print(f"{self.name}")


class Composite(Component):
	def __init__(self, *args, **kwargs):
		Component.__init__(*args, **kwargs)
		self.name = args[0]
		self.children = []

	def append_child(self, child):
		self.children.append(child)
		child.parent = self

	def remove_child(self, child):
		self.children.remove(child)

	def execute(self):
		print(f"Running {self.name}")
		for child in self.children:
			child.execute()

	def get_children(self):
		return self.children

	def get_child_index(self, child):
		if child not in self.children:
			return -1
		return self.children.index(child)
