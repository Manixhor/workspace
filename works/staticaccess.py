# class outer:
#     var = "I am a static in outside"

# print(outer.var)

#with inner class 

class Outer:
    static = "I am a static"

    class Inner:
        def show(self):
            print(Outer.static)
i = Outer.Inner()
i.show()