#UnorderedList

# A Node Class to store dat and link to next item
class Node:
	def __init__(self, item):
		self.data = item
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, newnext):
		self.next = newnext

	def setData(self, newdata):
		self.data = newdata


class UnorderedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		self.length = self.length+1

	def size(self):
		return self.length

	def search(self, item):
		current = self.head
		while current != None :
			if current.getData() == item:
				return True
			current = current.getNext()
		return False

	def remove(self, item):
		current = self.head
		previous = None
		while current != None :
			if current.getData() == item:
				break
			current = current.getNext()
		if previous == None:
			head = current.getNext()
		else:
			previous.setNext( current.getNext())

		self.length = self.length-1

	def __str__(self):
		current = self.head
		data = ""
		while current!=None:
			data = data+","+str(current.getData())
			current = current.getNext()
		return data


