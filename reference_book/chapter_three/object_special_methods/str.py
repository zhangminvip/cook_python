class Example(object):

    def __repr__(self):
        # super().__repr__()
        print('repr')
        return 'repr2'

    def __str__(self):
        print('str')
        return 'str2'

    def __format__(self, format_spec):
        print('format')
        return 'format2'

e = Example()
# str(e)   # screen out: str
print(e)   # screen out: str and str2
# format(e) # screen : format