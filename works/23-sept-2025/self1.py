class Main:
    def greet(self):
        print("Hey there")

hel = Main()

bound = hel.greet
print(bound.__self__)