class Vertex:

    def __init__(self, key):
    	self.id = key
    	self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None

    def addConnection(self, nbr, weight=0):
    	self.connectedTo[nbr] = weight

    def getConnections(self):
    	return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
            return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])\
                    +' color: '+ self.color + ' distance: '+ str(self.distance)

    def setColor(self, color):
        self.color = color

    def setDistance(self, value):
        self.distance = value

    def setPred(self, pred):
        self.pred = pred

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.pred


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addConnection(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        return '\n'.join(str(i) for i in self.vertList.values())
