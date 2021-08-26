class LinkedList(object):
	def __init__(self,first_node_data):
		self.head = Node(first_node_data)

	def __str__(self):
		node_number = 0
		runner = self.head
		while runner != None:
			print(node_number, runner.data, runner.nexter)
			node_number += 1
			runner = runner.nexter

	def add_node(self, input_data):
		tail = self.get_tail()
		tail.nexter = Node(input_data)
	def delete_head(self):
		self.head = self.nexter
	def get_tail(self):
		tracker = self.head
		while tracker:
			if tracker.nexter == None:
				return tracker
			else:
				tracker = tracker.nexter
	def get_len(self):
		counter = 0
		tracker = self.head
		while tracker:
			if tracker.nexter == None:
				return counter
			else:
				tracker = tracker.nexter
				counter += 1
	def sort(self):
		runner = self.head
		counter = 0
		while runner:
			if runner.nexter == None:
				self.sort()
			elif runner.data > runner.nexter.data:
				runner.data, runner.nexter.data = runner.nexter.data, runner.data
				runner = runner.next
				counter += 1
			else:
				runner = runner.next
				counter += 1
					if counter == self.get_len():
class Node(object):
	def __init__(self, input_data):
		self.data = input_data
		self.nexter = None

