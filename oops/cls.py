
class Human:
    name = None
    age = None
    wt = None
    height = None

    def sleep(self):
        print(self.name,"is sleeping")


person = Human()

person.name = "Ram"
person.Age = 1
person.height = 5
person.wt = 5

print(person.wt)


person2 = Human()

person2.name = "Gokul"
person2.Age = 1
person2.height = 5
person2.wt = 5

person.sleep()
person2.sleep()
