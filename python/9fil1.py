class Poly:
    def __init__(self,name):
        self.name = name

    def sleep(self,Sleeping = None, start = None, end = None):
        if start is not None & end is not None:
            print("sleep", abs(end-start))

        else:
            print("sleeping", Sleeping)

per1 = Poly(name="mani")
print(per1.name)