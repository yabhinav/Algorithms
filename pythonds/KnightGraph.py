from basic.graphs import Graph, Vertex

def KnightGraph(bdSize):
	ktGraph = Graph()
	for row in range(bdSize):
		for col in range(bdSize):
			nodeId = posToNodeId(row,col,bdSize)
			newPositions = genLegalMoves(row,col,bdSize)
			for e in newPositions:
				nid = posToNodeId(e[0],e[1],bdSize)
				ktGraph.addEdge(nodeId,nid)
	return ktGraph

# Convert location on board toa linear vertex number
def posToNodeId(row, column, board_size):
	return (row * board_size) + column

#  Generate all possible moves of the Knight
def genLegalMoves(x,y,bdSize) :
	newMoves = []
	moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)]
	for i in moveOffsets :
		newX = x + i[0]
		newY = y + i[1]
		if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
			newMoves.append((newY,newY))
	return newMoves

# Check Leaglity of row/column
def legalCoord(n,bdSize):
	if n>0 and n< bdSize:
		return True
	else:
		return False

def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


if __name__ == "__main__":

	kg = KnightGraph(8)
	#print kg
	path = []
	knightTour(0,path,kg.getVertex(0),6)
	print ' '.join(str(v) for v in path )

