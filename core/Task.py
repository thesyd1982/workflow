from time import sleep
from patterns.Composite import Component
import types
from patterns.State import Ready, Pause, Run, Finish, Resume, Init, Stop


class Task(Component):
	def __init__(self, name='Default TaskStrategy', function=None, data_input=None, data_output=None, check_ready=None):
		Component.__init__(self)
		self.parent = None
		self.name = name
		self.data_input = data_input
		self.data_output = data_output
		self.current_state = Init()

		# If a reference to a function is provided , repalace execute method by function
		if function:
			self.execute = types.MethodType(function, self)

		if check_ready:
			self.check_ready = types.MethodType(check_ready, self)

	def __repr__(self):
		return f'Task( name:{self.name},' \
			f' data_input:{self.data_input},' \
			f' data_output:{self.data_output},' \
			f' workflow: {self.get_workflow()} ) '

	def execute(self):
		print(f'-- Running {self.name} method')
		print('No input file') if not self.data_input else print(f'Input file {self.data_input}')
		print('No output file') if not self.data_output else print(f'Output file {self.data_output}')

	def save_workflow_result(self, result):
		workflow = self.get_workflow()
		if workflow:
			self.parent.results.append(result)

	def get_last_workflow_result(self):
		workflow = self.get_workflow()
		if workflow:
			return self.parent.results[-1]

	def get_workflow(self):
		return self.parent

	def check_ready(self):
		print(f"check_redy not implemented in :{self.name}")
		return True

	def set_state(self, state):
		list(self.current_state.go_next(state, debug=False))
		print(' __ ', self.current_state)

	def launch(self):
		self.ready(self.check_ready())
		self.run()

	def pause(self):
		self.set_state(Pause)
		sleep(5)

	def resume(self):
		self.set_state(Resume)
		self.set_state(Ready)
		self.set_state(Run)
		sleep(5)
		
	def run(self):
		self.set_state(Run)

	def stop(self):
		self.set_state(Stop)
		exit()

	def finish(self):
		self.set_state(Finish)

	def ready(self, is_ready=True):
		if not is_ready:
			self.stop()
		self.set_state(Ready)
