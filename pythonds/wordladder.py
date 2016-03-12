from basic.graphs import Graph, Vertex
from basic.Queue import Queue

def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile, 'r')

	# create bucket of words that differ by one letter
	for line in wfile:
		#print "word : "+line
		word = line[:-1]
		for i in range(len(word)):
			bucket =  word[:i]+'_'+word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]

	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2: # dont add edge to same vertices
					g.addEdge(word1,word2)

	return g

# Graph g and Vertex start (word to start search)
# we have solved  the problem for all words
def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


# Just traverse up to get thedistance between start word and y word
def traverse(y):
    x = y
    print  "Tranversing from End to Start :"
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print('Start :'+x.getId()+' End :'+y.getId()+' Distance'+str(y.getDistance()-x.getDistance()) )


if __name__ == "__main__":
	wordgraph = buildGraph('words')
	#bfs(wordgraph, wordgraph.getVertex('hell'))
	#print wordgraph
	#traverse(wordgraph.getVertex('fall'))
	bfs(wordgraph, wordgraph.getVertex('hole'))
	print wordgraph
	traverse(wordgraph.getVertex('fall'))

