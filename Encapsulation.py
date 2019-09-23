class Queue:
    def __init__(self, contents):
        self.hiddenlist = list(contents)

def push(self, value):
    self.hiddenlist.insert(0, value)

def pop(self):
    return self.hiddenlist.pop(-1)
def _show_list(self):
    return self.hiddenlist
queue: Queue =Queue([1,2,3])
print(queue.hiddenlist)
queue.push(0)
print(queue.hiddenlist)
queue.pop(0)
print(queue.hiddenlist)
print(queue.show_list())
