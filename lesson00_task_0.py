from user import User
from card import Card 

Jopa=User("jopa") # ну а здесь чисто уже присвоение  переменной Jopa в класс User 


Jopa.sayName() # а здесь буквально Jopa скажи как тебя зовут

Jopa.setAge(2222) # присвоение сколько лет -- setAge
Jopa.sayAge() # а здесь буквально Jopa скажи скока тебе лет, после присвоения setAge

card = Card ("1234 1254 1452 1452" , "11/99" ," Jopa J")

Jopa.addCard(card)
Jopa.getCard().pay(1000)
