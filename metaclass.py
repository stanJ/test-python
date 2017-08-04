class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass

class Foo(object):
    bar = True
def echo_bar(self):
    print(self.bar)
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
