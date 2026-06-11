#  Create a Hybrid Inheritance program: (3 Marks)
# • Father: property(), business()
# • Son(Father): study()
# • Daughter(Father): dance()
# • GrandChild(Son, Daughter): gaming()
# Create object of GrandChild and call ALL methods.

class Father:
    def Property(self):
        print("father owns flat")

    

class Son(Father):
     def study(self):
        print("Son is  studying")

class daughter(Father):
     def danc(self):
        print("Daughter is dancing")

class GrandChild(daughter,Son):
     def gaming(self):
        print("GrandChild is playing")

obj = GrandChild()
obj.gaming()
