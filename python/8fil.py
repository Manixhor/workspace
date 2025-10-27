class Person:
    def __init__(self):
        self.__name = None

    def SetName(self,Value):
        if len(Value) > 20:
            print("can't be more than 20")
        else:
            self.__name = Value

    def GetName(self):
        return self.__name

per = Person()
per.SetName("manifjdbfkjbvdfvdvcfdvcfjkbvfd")
print(per.GetName())