class User: # создание класса User

    age=4444


    def __init__(self, name): # конструктор с принт еремин казел и присвоением self username
        print ("еремин казел :")
        self.username = name # self.username длы метода принта в sayName

    def sayName(self):
        print ("меня зовут :" , self.username)

    def sayAge(self):
        print(" Мне сейчас " , self.age)

    def setAge(self,newAge):
        self.age = newAge
        
    def addCard(self,card):
        self.card=card

    def getCard(self):
        return self.card
    
    
    
    



