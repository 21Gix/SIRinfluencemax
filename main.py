class Node:
    def __init__(self, id, status):
        self.id = id
        self.status = status


class Msg:
    def __init__(self, id, src, dest, eta):
        self.id = id
        self.src = src
        self.dest = dest
        self.eta = eta


if __name__ == '__main__':
    filename = input('Enter the filename for the dataset: ')

    print('Opening file ', filename, ':')
