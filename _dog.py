class Dog:
    def __init__(self,name,age,coatColor):
        self.name = name
        self.age = age
        self.coatColor = coatColor

    def description(self):
        print(f"name : {self.name} \n Age : {self.age}")

    def getInfo(self):
        print(f"Coat color : {self.coatColor}")

class JackRussellTerrier(Dog):

    def __init__(self, name, age, coatColor):
        super().__init__(name, age, coatColor)

    def bark(self,sound):
        self.sound = sound
        print(f"Sound : {self.sound}")

    def height(self,height):
        self.height = height
        print(f"Dog Height: {self.height}")

class Bulldog(Dog):

    def bark(self,sound):
        self.sound = sound
        print(f"Sound : {self.sound}")

    def height(self,length):
        self.length = length
        print(f"Dog Height : {self.length}")


i_obj = JackRussellTerrier("lachu",20,"green")
i_obj.description()
i_obj.getInfo()
i_obj.bark("arf")
i_obj.height(56)

u_obj = Bulldog("Peri", 4,"brown")
u_obj.description()
u_obj.getInfo()
u_obj.bark("hush")
u_obj.height(60)
