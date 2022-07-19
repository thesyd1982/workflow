from enum import Enum


class STATUS(Enum):
	INIT = 0
	READY = 1
	RUNNING = 2
	PAUSED = 3
	STOPED = 4
	FINISHED = 5
	RESUMED = 6
	ERROR = 7
pass


class TaskState:
	name = 'state'
	allowed = []

	def go_next(self, state, debug=False):
		if state.name in self.allowed:
			if debug:
				print("Current State:", self, " switched to: ", state.name)
			self.__class__ = state
			yield
		else:
			if debug:
				print("Current State:", self, " switched to: ", state.name, 'not possible!')

	def __str__(self):
		return self.name


class Init(TaskState):
	name = STATUS.INIT.name
	allowed = [STATUS.READY.name, STATUS.STOPED.name]
	pass


class Ready(TaskState):
	name = STATUS.READY.name
	allowed = [STATUS.RUNNING.name, STATUS.STOPED.name]
	pass


class Pause(TaskState):
	name = STATUS.PAUSED.name
	allowed = [STATUS.RESUMED.name, STATUS.STOPED.name]
	pass


class Resume(TaskState):
	name = STATUS.RESUMED.name
	allowed = [STATUS.READY.name, STATUS.STOPED.name]
	pass


class Run(TaskState):
	name = STATUS.RUNNING.name
	allowed = [STATUS.PAUSED.name, STATUS.FINISHED.name, STATUS.STOPED.name]
	pass


class Stop(TaskState):
	name = STATUS.STOPED.name
	allowed = [STATUS.FINISHED]
	pass


class Finish(TaskState):
	name = STATUS.FINISHED.name
	allowed = [STATUS.INIT.name]
	pass


class WorkflowState:
	name = 'state'
	allowed = []

	def go_next(self, state):

		if state.name in self.allowed:
			print("Current State:", self, " switched to: ", state.name)
			self.__class__ = state
		else:
			print("Current State:", self, " switched to: ", state.name, 'not possible!')

	def __str__(self):
		return self.name


