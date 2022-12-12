import random


class Node:
    def __init__(self, id, status, vulnerability):
        self.id = id
        self.status = status
        self.vulnerability = vulnerability

    def __str__(self):
        return 'Nodo: ' + str(self.id) + ', Stato: ' + str(self.status)


class Msg:
    def __init__(self, id, src, dst, eta):
        self.id = id
        self.src = src
        self.dst = dst
        self.eta = eta

    def __str__(self):
        return 'Mittente: ' + str(self.src.id) + ', Destinatario: ' + str(self.dst.id) + ', Eta: ' + str(self.eta)


if __name__ == '__main__':
    filename = input('Enter the filename for the dataset(must be .txt): ')

    # dataset import
    print('Opening file :', filename)
    try:
        f = open(filename, 'r')
    except:
        print('File non esistente')
        quit()

    # populating lists
    nodeList = []
    msgList = []
    j = 1
    for line in f:
        i = 1
        for w in line.split():
            if i == 3:
                times = w
            elif i == 2:
                destination = w
                nodoD = Node(int(destination), 0, 0.5)
                if sum(nodo.id == int(destination) for nodo in nodeList) == 0:
                    nodeList.append(nodoD)
            elif i == 1:
                source = w
                nodoS = Node(int(source), 0, 0.5)
                if sum(nodo.id == int(source) for nodo in nodeList) == 0:
                    nodeList.append(nodoS)
            i = i + 1

        msgList.append(Msg(j, nodoS, nodoD, int(times)))
        j = j + 1

    # close file
    f.close()
    # sort messages list based on eta
    msgList.sort(key=lambda x: x.eta)

    # sort node list based on node id
    nodeList.sort(key=lambda x: x.id)

    # input infected nodes
    inpt = input('Insert node to be infected ("stop" to start simulation): ')
    while inpt != 'stop' and inpt != 'STOP':
            found = False
            try:
                intero = int(inpt)
                for elem in nodeList:
                    if int(elem.id) == intero:
                        found = True
                        elem.status = -1

                if found:
                    print('Infected node: ', intero)
                    for elem in msgList:
                        if int(elem.src.id) == intero:
                            elem.src.status = -1
                        if int(elem.dst.id) == intero:
                            elem.dst.status = -1

                else:
                    print('Node: ', intero, ' does not exist')
            except:
                print('Insert integer number')

            inpt = input('Insert node to be infected ("stop" to start simulation): ')

    # simulation of infection
    print('simulating....this could take a while')
    stdEngagement = 1
    stdTrust = 0.4
    pRecover = 0

    for msg in msgList:
        indxM = msgList.index(msg)

        for node in nodeList:
            if msg.src.id == node.id:
                indxS = nodeList.index(node)
            if msg.dst.id == node.id:
                indxD = nodeList.index(node)

        if nodeList[indxS].status == -1 and nodeList[indxD].status == 0:
            pspread = stdEngagement*stdTrust*nodeList[indxD].vulnerability

            if random.uniform(0,1) < pspread:
                nodeList[indxD].status = -1
                msgList[indxM].dst.status = -1
            elif random.uniform(0,1) < pRecover:
                nodeList[indxD].status = 1
                msgList[indxM].dst.status = 1

        elif nodeList[indxS].status == 1 and nodeList[indxD].status != 1:
            pspread = stdEngagement/3 * stdTrust * nodeList[indxD].vulnerability

            if random.uniform(0,1) < pspread:
                nodeList[indxD].status = 1
                msgList[indxM].dst.status = 1

    # Deploy results
    nInfected = 0
    nRecovered = 0
    nSusceptible = 0
    nNodes = 0
    for node in nodeList:
        nNodes += 1
        if node.status == 0:
            nSusceptible += 1
        elif node.status == -1:
            nInfected += 1
        else:
            nRecovered += 1

    print('Simulation ended with: ', nNodes, ' nodes')
    print('Infected: ', nInfected)
    print('Susceptible: ', nSusceptible)
    print('Recovered: ', nRecovered)











