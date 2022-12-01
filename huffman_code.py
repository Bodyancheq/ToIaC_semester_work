def find_char_frequency(text):
    result = []

    with open(text, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                chars = line.strip("\n").split(" ")
                result = [[char] for char in chars]
            elif i == 1:
                for i, prob in enumerate(line.split(" ")):
                    result[i].append(float(prob))
    return dict(result)


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, char_weights: dict):
        self.Leafs = [Node(k, v) for k, v in char_weights.items()]
        while len(self.Leafs) != 1:
            self.Leafs.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leafs[-1].value + self.Leafs[-2].value))
            n.lchild = self.Leafs.pop(-1)
            n.rchild = self.Leafs.pop(-1)
            self.Leafs.append(n)

        self.root = self.Leafs[0]
        self.Buffer = list(range(10))

    def Hu_generate(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print("Кодировка Хаффмана " + node.name, end=': ')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.Hu_generate(self.root, 0)


if __name__ == '__main__':
    text = r'text.txt'
    result = find_char_frequency(text)
    print(result)
    tree = HuffmanTree(result)
    tree.get_code()
