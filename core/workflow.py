from patterns.Composite import Composite
from patterns.State import Ready


class Workflow(Composite):
	count = 0

	def __init__(self, name=None):
		self.results = []
		self.current_state = Ready()
		if name:
			Composite.__init__(self, name)
		else:
			Workflow.count += 1
			name = 'Workflow ' + str(Workflow.count)
			Composite.__init__(self, name)

	def __repr__(self):
		return f'Wrokflow(count: {Workflow.count}, result: {self.results}, name: {self.name})'

	def execute(self):
		print(f"Running {self.name}")
		for child in self.children:
			self.results.append(child.execute())

	def get_result(self):
		return self.results

	def get_last_result(self):
		return self.results[-1]

	def set_result(self, res):
		self.results.append(res)

	def set_state(self, state):
		self.current_state.go_next(state)