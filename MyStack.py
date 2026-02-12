class MyStack:
    ## data
    def __init__(self):
        self.data = []
	## funcionaliteit:
    def isEmpty(self):
        return(len(self.data) == 0)

    def getTop(self):
        if self.data:
            return (self.data[-1], True)
        return (None, False)

    def pop(self):
        if self.data:
            return (self.data.pop(), True)
        return (None, False)

    def push(self, item):
        self.data.append(item)
        return (True)

    def save(self):
        return self.data.copy()

    def load(self, data):
        if (data, list):
            self.data = data.copy()
            return (True)
        return (False)