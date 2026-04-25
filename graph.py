class Graph:
    def __init__(self):
        self.start_point = 0
        self.destination = []
        self.coordinates = {}
        self.edges = {}

    def loadFile(self, fileName):
        lindex = 0
        with open(fileName,"r") as file:
            for line in file.readlines():
                line = line.strip()
                self.stringProcess(lindex,line)
                lindex+=1

    def stringProcess(self,index, fileLine):
        if (index == 0):
            self.start_point = int(fileLine)
        elif (index == 1):
            self.destination = [int(x) for x in fileLine.split(";")]
        elif ':' in fileLine:
            self.handle_coordinate(fileLine)
        elif ',' in fileLine:
            self.handle_edges(fileLine)
    
    def handle_coordinate(self, fileLine):
        node, point = fileLine.split(":")
        node = int(node)

        point = point.strip("()")
        x, y = point.split(",")

        self.coordinates[node] = (int(x), int(y))

        if node not in self.edges:
            self.edges[node] = []


    def handle_edges(self, fileLine):
        start, end, cost = fileLine.split(",")
        start = int(start)
        end = int(end)
        cost = int(cost)

        if start not in self.edges:
            self.edges[start] = []

        if end not in self.edges:
            self.edges[end] = []

        self.edges[start].append((end, cost))


