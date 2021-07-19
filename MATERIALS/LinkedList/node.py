class Node(object):
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	# Get methods
	def get_next(self):
		return self.next

	def get_data(self):
		return self.data

	# Set methods
	def set_next(self, next):
		self.next = next

	def set_data(self, data):
		self.data = data
