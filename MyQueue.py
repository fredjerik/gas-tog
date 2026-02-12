class MyQueue:
    ## data
    def __init__(self):
        self.data = []
	## funcionaliteit:
    def isEmpty(self):
        return(len(self.data) == 0)

    def getFront(self):
        if self.data:
            return (self.data[-1], True)
        return (None, False)

    def dequeue(self):
        if self.data:
            return (self.data.pop(), True)
        return (None, False)

    def enqueue(self, item):
        self.data.insert(0,item)
        return (True)

    def save(self):
        return self.data.copy()

    def load(self, data):
        if (data, list):
            self.data = data.copy()
            return (True)
        return (False)