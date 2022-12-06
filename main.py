class Node:
    def __init__(self, id, status):
        self.id = id
        self.status = status


class Msg:
    def __init__(self, id, src, dst, eta):
        self.id = id
        self.src = src
        self.dst = dst
        self.eta = eta


if __name__ == '__main__':
    filename = input('Enter the filename for the dataset(must be .txt): ')

    # dataset import
    print('Opening file :', filename)
    f = open(filename, 'r')

    # preparing messages list
    msgList = []

    for x in f:
        print(x, end='')
