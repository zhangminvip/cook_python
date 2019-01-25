class Example():

    def __init__(self, val):
        self.value = val

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    def __hash__(self):
        print('id / 6 : ', id(self) / 6)
        return int(id(self) / 6)


e = Example(7)
d = Example(7)
r = Example(8)
print(e == d)
print(e == r)
print(hash(e))
