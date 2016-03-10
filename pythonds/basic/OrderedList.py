from UnorderedList import UnorderedList

class OrderedList(UnorderedList):

    def __init__(self):
    	self.head = None
    	UnorderedList.__init__(self)

	def search(self, item):
		current = self.head
		stop = False
		while current != None and stop:
			if current.getData() == item:
				return True
	        else :
	        	if current.getData() > item:
	        		stop = True
	        	else:
	        		current = current.getNext()

		return False

	def add(self, item):
	    current = self.head
	    previous = None
	    while current != None :
	        if current.getData() > item:
	            break
	        else:
	            previous = current
	            current = current.getNext()

	    temp = Node(item)
	    if previous == None:
	        temp.setNext(self.head)
	        self.head = temp
	    else:
	        temp.setNext(current)
	        previous.setNext(temp)
	    self.length = self.length+1

