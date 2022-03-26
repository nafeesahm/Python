"""Sometimes we can declare a class inside another class, such type of classes are called
inner classes."""

class outer:
    def __init__(self):
        print("outer class object created")

    class inner:
        def __init__(self):
            print("inner class object created")

        def m1(self):
            print("inner class method")

# o = outer()
# i = o.inner()
# i.m1()

# i = outer().inner()
# i.m1()

outer().inner().m1()

