## 继承
### 1.定义
* 1.子类不用写，但是可以用，重用现有类的功能与概念，并在此基础上进行扩展。
* 2.说明：  
  --子类直接具有父类的成员（共性），还可以扩展新功能。  
  --事物具有一定的层次、渊源，继承可以统一概念。 
  --多个子类的共性可以提取到父类中  
    在实际开发过程中，从设计角度讲，先有子，再有父;从编码角度讲，先有父，再有子   
### 2.语法
```
# 定义父类
class Person:
    def say(self):
        print("说话...")
        
# 定义子类，继承Person类
class Student(Person):
    def study(self):
        print("学习...")

class Teacher(Person):
    def teach(self):
        print("讲课...")

stu = Student()
# 子类对象可以调用子类成员，也可以调用父类成员
stu.study()
stu.say()

# python 内置 isinstance 判断对象是否属于一个类型
print(isinstance(stu, Person))  # True
print(isinstance(stu, Teacher))  # False
# python 内置 issubclass 判断一个类型是否属于另一个类型
print(issubclass(Student, Person))  # True
print(issubclass(Person, Student))  # False
```
### 3.设计原则
* 1.开-闭原则（目标、总的指导思想）  
  Open Closed Principle  
  对扩展开放，对修改关闭。  
  增加新功能，不改变原有代码。
* 2.类的单一职责（一个类的定义）  
  Single Responsibility Principle       
  一个类有且只有一个改变它的原因。
* 3.依赖倒置（依赖抽象）  
  Dependency Inversion Principle  
  客户端代码(调用的类)尽量依赖(使用)抽象的组件。  
  抽象的是稳定的。实现是多变的。
* 4.组合复用原则（复用的最佳实践）  
  Composite Reuse Principle  
  如果仅仅为了代码复用优先选择组合复用，而非继承复用。  
  组合的耦合性相对继承低。

## 类与类的关系
* 1.泛化：子类与父类的关系，概念的复用，耦合度最高；  
  B类泛化A类，意味B类是A类的一种；  
  做法：B类继承A类 

* 2.关联(聚合/组合)：部分与整体的关系，功能的复用，变化影响一个类；  
  A与B关联，意味着B是A的一部分；  
  做法：在A类中包含B类型成员。 

* 3.依赖：合作关系，一种相对松散的协作，变化影响一个方法；  
  A类依赖B类，意味A类的某些功能靠B类实现；  
  做法：B类型作为A类中方法的参数，并不是A的成员。
 
## 多态
* 定义：父类的同一种动作或者行为，在不同的子类上有不同的实现。
* 作用：  
  1.继承将相关概念的共性进行抽象，多态在共性的基础上，体现类型的个性化(一个行为有不同的实现)  
  2.增强程序扩展性，体现开闭原则。
