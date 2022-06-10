class Graph:
    def __init__(self):
        self.nodes = [
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

        self.count = range(len(self.nodes))

    def GetInputNodesArray(self):
        array = []
        for i in self.count:
            step = 0
            for j in self.count:
                if self.nodes[i][j] == 1: step += 1
            array.insert(i, step)
        return array

    def TopologicSort(self):
        result = []
        workArray = self.GetInputNodesArray() #получаем список степеней вершин
        while (len(result) != len(self.nodes)):
            for i in range(len(self.nodes)):
                if (workArray[i] == 0): #если вершина не имеет входящих ребер
                    print(workArray)
                    result.append(i + 1) #добавляем обработанную вершину в список
                    for node in self.nodes: #для каждой вершины
                        if node[i] == 1: #если вершина имелла исходящее ребро в обработаную
                            workArray[self.nodes.index(node)] -= 1 #снижаем ее степень
                    workArray[i] = -1 #помечаем обработаную вершину
        return result


steps = {"А": "Добавить лук к ципленку",
         "Б": "Вымыть салат-латук",
         "В": "Приготовить салатную заправку",
         "Г": "Перемешать жаркое и лист",
         "Д": "Перемешать салат",
         "Е": "Расчленить цыпленка",
         "Ж": "Растереть имбирь",
         "З": "Подать готовое блюдо",
         "И": "Замариновать цыпленка",
         "К": "Поставить казанок на огонь",
         "Л": "Приготовить рис"
         }

graph = [[1, 2], [2, 3], [1, 4], [2, 3], [1, 9], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]]
cycles = []


def findShortestCycles():
    global graph
    global cycles

    for edge in graph:
        for node in edge:
            findNewCycles([node])
    print("Кратчайшие циклы:")
    for cy in cycles:
        if len(cy) == len(min(cycles)):
            path = [str(node) for node in cy]
            s = ",".join(path)
            print(s)

def findNewCycles(path):
    start_node = path[0] #последняя вершина в пути

    # visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge: #проверка на наличие начала пути в ребре что бы вершина не составляла цикл сама с собой
            if node1 == start_node:
                next_node = node2
            else:
                next_node = node1
            if not visited(next_node, path): #если вершина еще не в цикле
                # explore extended path
                findNewCycles([next_node] + path) #переход к следуйщей вершине
            elif len(path) > 2 and next_node == path[-1]: #если в процессе рекурсии
                # cycle found
                p = rotate_to_smallest(path)
                inv = invert(p)
                if isNew(p) and isNew(inv):
                    cycles.append(p)


def invert(path):
    return rotate_to_smallest(path[::-1])


#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:] + path[:n]


def isNew(path):
    return not path in cycles


def visited(node, path):
    return node in path

steps = {1: "Добавить лук к ципленку",
         2: "Вымыть салат-латук",
         3: "Приготовить салатную заправку",
         4: "Перемешать жаркое и лист",
         5: "Перемешать салат",
         6: "Расчленить цыпленка",
         7: "Растереть имбирь",
         8: "Подать готовое блюдо",
         9: "Замариновать цыпленка",
         10: "Поставить казанок на огонь",
         11: "Приготовить рис"
         }

list = Graph().TopologicSort()
print(list)
for i in range(len(list)):
    print(f"{i + 1}: {steps.get(list[i])}")

findShortestCycles()