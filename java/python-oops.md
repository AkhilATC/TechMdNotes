# Object oriented programming in Python 


```python
# Simple class 
class MusCat:
    name = "Mus"
    icon = "🐈"
    
    def mus_say_hello():
        return f"Mwow Mwow"
```


```python
# Now we need to create a instance of MusCat class
mus = f"{MusCat.name} {MusCat.icon} : {MusCat.mus_say_hello()}"
# here we access class member varaiable and member function using instance of a class
mus 
c =  MusCat()
```

### self keyword


```python
# self- referance python member function accept object of a class as argument
class RatKing():
    def __str__():
        return "🐀 king is lived here ...!!!!"
a =  RatKing()
str(a) # This will raise a exception - TypeError: __str__() takes 0 positional arguments but 1 was given
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [33], in <cell line: 6>()
          4         return "🐀 king is lived here ...!!!!"
          5 a =  RatKing()
    ----> 6 str(a)


    TypeError: __str__() takes 0 positional arguments but 1 was given



```python
# Why this happend? memeber functions of class expect its own object so rewrite as follow
class RatKing():
    def __str__(self):
        return "🐀 king is lived here ...!!!!"
a =  RatKing()
str(a)
```




    '🐀 king is lived here ...!!!!'



### class method 


```python
class Donut():
    instance = []
    def __init__(self):
        self.instance.append(self)
a =  Donut()
b = Donut()
print(len(a.instance)) # created instance count
```

    2



```python
# now we can create a class method
class Frog():
    
    def __init__(self,name):
        self.name = name
        
    @staticmethod
    def sayMaName():
        print(f"Hello its me ")
    @classmethod
    def cool(cls):
        cls.sayMaName()
a =  Frog("Makku")
Frog.sayMaName()
a.cool()
```

    Hello its me 
    Hello its me 


## Object

An object consists of : 

- State: It is represented by the attributes of an object. It also reflects the properties of an object.
- Behaviour: It is represented by the methods of an object. It also reflects the response of an object to other objects.
- Identity: It gives a unique name to an object and enables one object to interact with other objects.


```python
class monkey:
    family = "Cercopithecidae"
    
    def print_info(self):
        print(f"🐒 : I'm belogs to {self.family}")
    def print_say_ma_name(self):
        print(f"🐒: kola")
    @staticmethod
    def say_ma_age(dob):
        return 2022 - dob
        
# object
kola =  monkey()
print(kola.family) # access monkey class attribute
print(kola.print_info())
print(kola.print_say_ma_name())
print(kola.__dict__)
print(monkey.say_ma_age(1995))
print(monkey().print_info())
```

    Cercopithecidae
    🐒 : I'm belogs to Cercopithecidae
    None
    🐒: kola
    None
    {}
    27
    🐒 : I'm belogs to Cercopithecidae
    None


### class variable and instance variable



```python
class Car:
    type_ = "Racing car 🏎️ " # class variable  
    def __init__(self,model,speed):
        self.model = model # instance variable
        self.speed =  speed
        
# define a object of class car
drift_v1 = Car("FireExtnted","240 km/hr")
print(f"{drift_v1.type_} - {drift_v1.model} - {drift_v1.speed}")
Car.type_ # class variable we can access via class name
# Car.model throws error AttributeError: type object 'Car' has no attribute 'model'
```

    Racing car 🏎️  - FireExtnted - 240 km/hr





    'Racing car 🏎️ '



## Constructor

Types of constructors : 

1. default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
2. parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.



```python
class Monkey:
    def __init__(self,name): # init function
        self.name = name
   
    def say_ma_name(self):
        return f"🐒 {self.name} "

m = Monkey("KokA")
print(m.say_ma_name())
        
```

    🐒 KokA 


### Destructors in Python
Destructors are called when an object gets destroyed. 
In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.


```python
class Monkey:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print("Done--->🐒 i'm going to trash")
        
m = Monkey("ddk")
print("done")
del m
```

    done
    Done--->🐒 i'm going to trash



```python
class Monkey:
    def __init__(self,name):
        print("init")
        self.name = name
    def __del__(self):
        print("Bye BYE")
def give_a_monkey():
    return Monkey("Akui")
a = give_a_monkey()
print("final--")
```

    init
    Bye BYE
    here


## Inheritance in python


```python
# Parent class
class Man(object):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def call_me1(self):
        print(f"COOL {self.name} {self.age} created...")
  
    
```


```python
# Now we can create a child/sub class
class Runner(Man):
    
    def call_me(self):
        print("---- BASE CLASS RUNNER Called ....")

man2 = Runner("John",10)
man2.call_me1() # access parent method
        
```

    COOL John 10 created...



```python
# init parent class
class Rider(Man):
    def __init__(self,name,age,gadgets):
        
        self.gadgets = gadgets
        Man.__init__(self,name,age)
    
c =  Rider("Apsb",12,"nn")
c.__dict__
```




    {'gadgets': 'nn', 'name': 'Apsb', 'age': 12}



- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
- Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 
- Multilevel inheritance: When we have a child and grandchild relationship. 
- Hierarchical inheritance More than one derived class are created from a single base.


## Encapsulation in Python


__Private members__ in python initialize member variable starting with '__' double underscore 


```python
class School(object):
    def __init__(self):
        self.__bus = "🚌" #private variable
        self.whiteboard = "White board 🪪" 
class Student(School):
    def __init__(self):
        #print(self.__bus)
        School.__init__(self)
        print(self.whiteboard) # this will work
        print(self.__bus) # can't access private variable
        
a = Student()
```

    White board 🪪



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Input In [48], in <cell line: 12>()
          9         print(self.whiteboard) # this will work
         10         print(self.__bus)
    ---> 12 a = Student()


    Input In [48], in Student.__init__(self)
          8 School.__init__(self)
          9 print(self.whiteboard) # this will work
    ---> 10 print(self.__bus)


    AttributeError: 'Student' object has no attribute '_Student__bus'


## Polymorphism in Python


What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.


```python
# polymorphism in build in functions
print(len("akiknoi"))
print(len([1,2,3,4]))
```

    7
    4


