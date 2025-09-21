class Mom:
    def give(self):
        print("mom gives chocolate")
class Dad:
    def give(self):
        print("dad gives chocolate")
class Grand:
    def give(self):
        print("grand gives chocolate")

class Child(Mom,Dad,Grand):
    pass

child1 = Child()
child1.give()