from basic.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph]) # Buiding a min Heap
    while not pq.isEmpty():
        currentVert = pq.delMin() # Get the V with min distance from start and not visited
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance(): # Old one is infinity if not visited before
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

