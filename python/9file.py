class poly:
    def __init__(self,name,age):
    
        self.name = name 
        self.age = age

    # def sleep(self,sleep):
    #     print("sleeping",sleep)
    def sleep(self,start,end):
        print("sleep",abs(end-start))
   

        

pers = poly(20,"ashok")

pers.sleep(2,4)