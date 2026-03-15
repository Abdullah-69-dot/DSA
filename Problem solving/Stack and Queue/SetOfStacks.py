class Setofstacks:
    def __init__(self,capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.history = []

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return self.count()

    def __iter__(self):
        return iter(self.stack)

    def count(self):
        i = 0
        while i < len(self.stack):
            if self.stack[i] is not None:
                i += 1
            else:
                break
        return i

    def push(self,item):

        if not self.IsCapacityReached():
            self.stack[self.count()] = item

        else:
            newcapacity = self.capacity * 2
            newstack = [None] * newcapacity

            for i in range(self.capacity):
                newstack[i] = self.stack[i]

            self.history.append(self.stack.copy())

            self.stack = newstack
            self.capacity = newcapacity

            self.stack[self.count()] = item

    def pop(self):
        index = self.count() - 1

        if index < 0:
            return None

        val = self.stack[index]
        self.stack[index] = None
        return val

    def IsCapacityReached(self):
        return self.count() == self.capacity
customstack = Setofstacks(3)
customstack.push(2)
customstack.push(1)
customstack.push(3)
customstack.push(4)
customstack.push(5)
customstack.push(6)
customstack.push(7)

print(customstack)