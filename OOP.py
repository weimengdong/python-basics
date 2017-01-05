# Python学习笔记（OOP）：面向对象 


# 大型程序，通常采用面向对象编程。类和对象是面向对象编程的两个主要方面，类创建一个新类型，而对象是类的实例。
# Python没有什么值类型与引用类型之分，它把所有事物统统看作是类。类使用class关键字来创建。

1. Self

# 类的方法与普通的函数只有一个特别的区别: 必须有一个额外的第一个参数名称，调用这个方法,Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self。假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法MyObject.method(arg1, arg2)的时候，这会由Python自动转为MyClass.method(MyObject, arg1, arg2)——这就是self的原理了。

2. 类

# 一个空类：
class Person:
    pass #An empty block 
# 类的使用：
p= Person()
print(p) 

3. 方法

#类/对象可以拥有像函数一样的方法，这些方法与函数的区别只是一个额外的self变量。
class Person:
    def sayHi(self):
        print("Hello, how are you?")
p = Person()
p.sayHi() 
# 注意调用sayHi方法时没有任何参数，但仍然在函数定义时有self。

4. __init__方法

# 在Python的类中有很多方法的名字有特殊的重要意义。像__init__，类似于构造函数。__init__方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的初始化 。注意，这个名称的开始和结尾都是双下划线。
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hello, my name is", self.name)
p = Person("known")
p.syaHi() 

5. 域

Python有两种类型的域——类的变量和对象的变量，它们根据是类还是对象拥有这个变量而区分。
类的变量由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以当某个对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
对象的变量由类的每个对象/实例拥有。因此每个对象有自己对这个域的一份拷贝，即它们不是共享的，
在同一个类的不同实例中，虽然对象的变量有相同的名称，但是是互不相关的。

class Person:

    '''Represnets a person.'''

    population = 0

 
    def __init__(self, name):

        '''Initializes the person's data.'''

        self.name = name

        print("(Initializing %s)" % self.name)

 
        #When this person is created, he/she adds to the population

        Person.population += 1

 

    def __del__(self):

        '''I am dying.'''

        print("%s says bye." % self.name)

 

        Person.population -= 1

 

        if Person.population == 0:

            print("I am the last one.")

        else:

            print("There are still %d people left." % Person.population)
 

    def sayHi(self):

        '''Greeting by the person.

          Really, that's all it does.'''

        print("Hi, my name is %s." % self.name)

 

    def howMany(self):

        '''Prints the current population.'''

;
swaroop.howMany()

 

kalam = Person('Abdul Kalam')

kalam.sayHi()

kalam.howMany()

 

swaroop.sayHi()

swaroop.howMany()

 

del kalam

del swaroop 

运行结果：

(Initializing Swaroop)
Hi, my name is Swaroop.
I am the only person here.
(Initializing Abdul Kalam)
Hi, my name is Abdul Kalam.
We have 2 persons here.
Hi, my name is Swaroop.
We have 2 persons here.
Abdul Kalam says bye.
There are still 1 people left.
Swaroop says bye.
I am the last one.

6. 继承
# 在类名后面跟一对圆括号，基类名写在圆括号内。
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember: %s)" % self.name)

    def tell(self):
        '''Tell my details.'''
        print("Name:'%s' Age:'%s'" % (self.name, self.age))


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initialized Teacher: %s)" % self.name)
        
    def tell(self):
        SchoolMember.tell(self)
        print("Salary: '%d'" % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Initialized Student: %s)" % self.name)
    
    def tell(self):
        SchoolMember.tell(self)
        print("Marks: '%d'" % self.marks)
        
t = Teacher("Mrs. Shrividya", 40, 30000)
s = Student("Swaroop", 22, 75)

print() # prints a blank line
members = [t, s]

for member in members:
    member.tell() # works for both Teachers and Students 

输出结果：

(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)
