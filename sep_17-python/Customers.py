class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return f"my Firstname is {self.firstname} and my Lastname is {self.lastname}"
      
#create objects of the class
c1 = Customer('Arun','Prasath')
c2 = Customer('Yogi','Babu')

#call methods
print(c1.name())
print(c2.name())
