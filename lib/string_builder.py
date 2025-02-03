class StringBuilder:
    def __init__(self):
        self.string = ""

    def add(self, string):
        self.string += string

    def size(self):
        return len(self.string)

    def output(self):
        return self.string
