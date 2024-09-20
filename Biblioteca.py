class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        return None

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        return None

    def empty(self):
        return len(self.items) == 0

    def travel(self):
        return self.items

    def search(self, item):
        return item in self.items


class Lista:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def search(self, item):
        return item in self.items

    def travel(self):
        return self.items
