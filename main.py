class Node:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def __str__(self):
        return 'Nodo: ' + str(self.id) + ', Stato: ' + str(self.status)


class Msg:
    def __init__(self, id, src, dst, eta):
        self.id = id
        self.src = src
        self.dst = dst
        self.eta = eta

    def __str__(self):
        return 'Mittente: ' + self.src + ', Destinatario: ' + self.dst + ', Eta: ' + self.eta


if __name__ == '__main__':
    filename = input('Enter the filename for the dataset(must be .txt): ')

    # dataset import
    print('Opening file :', filename)
    f = open(filename, 'r')

    # preparing lists
    msgList = []
    nodeList = []

    # support variables
    ident = 0
    source = 0
    destination = 0
    times = 0
    j = 1

    # populate messages list
    for x in f:
        i = 1
        for w in x.split():
            if i % 3 == 0:
                times = w
            elif i % 2 == 0:
                destination = w
                if sum(nodo.id == w for nodo in nodeList) == 0:
                    nodeList.append(Node(w, 0))
            else:
                source = w
                if sum(nodo.id == w for nodo in nodeList) == 0:
                    nodeList.append(Node(w, 0))
            i = i + 1
        msgList.append(Msg(j, source, destination, times))
        j = j + 1

    # sort messages list based on eta
    msgList.sort(key=lambda x: x.eta, reverse=False)

    for msg in msgList:
        print(str(msg))

    for us in nodeList:
        print(str(us))

