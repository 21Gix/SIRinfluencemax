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
        return 'Mittente: ' + str(self.src) + ', Destinatario: ' + str(self.dst) + ', Eta: ' + str(self.eta)


def messagelist(file):
    # support variables
    l = []
    source = 0
    destination = 0
    times = 0
    j = 1

    # populate messages list
    for line in f:
        i = 1
        for w in line.split():
            if i % 3 == 0:
                times = w
            elif i % 2 == 0:
                destination = w
            else:
                source = w
            i = i + 1
        l.insert(j, Msg(j, int(source), int(destination), int(times)))
        j = j + 1

    return l


def nodelist(messages):
    # support variables
    m = []

    for sms in messages:
        if sum(nodo.id == sms.src for nodo in m) == 0:
            m.insert(int(sms.src), Node(int(sms.src), 0))
        if sum(nodo.id == sms.dst for nodo in m) == 0:
            m.insert(int(sms.dst), Node(int(sms.dst), 0))

    return m


if __name__ == '__main__':
    filename = input('Enter the filename for the dataset(must be .txt): ')

    # dataset import
    print('Opening file :', filename)
    f = open(filename, 'r')

    # populating lists
    msgList = messagelist(f)
    nodeList = nodelist(msgList)

    # close file
    f.close()

    # sort messages list based on eta
    msgList.sort(key=lambda x: int(x.eta))

    # sort node list based on node id
    nodeList.sort(key=lambda x: int(x.id))

    # input infected nodes
    inpt = input('Insert node to be infected ("stop" to start simulation): ')
    while inpt != 'stop' and inpt != 'STOP':
            found = False
            try:
                intero = int(inpt)
                for elem in nodeList:
                    if elem.id == intero:
                        found = True
                        elem.status = -1
                if found:
                    print('Infected node: ', intero)
                else:
                    print('Node: ', intero, ' does not exist')
            except:
                print('Insert integer number')

            inpt = input('Insert node to be infected ("stop" to start simulation): ')

    # simulation of infection
    for nd in nodeList:
        print(str(nd))
