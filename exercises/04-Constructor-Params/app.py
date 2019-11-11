class Person:
    def __repr__(self):
        return '{Name:'+' '+self.name+', Last Name:'+' '+str(self.last_name)+', Birth Date:' +' '+ str(self.birth_date) +'}'
    # CHANGE ONLY THE CONSTRUCTOR FUNCTION
    def __init__ (self, name, last, date) :
        self.name = "Bob"
        self.last_name = "Dylan"
        self.birth_date = "May 24, 1941"

# DON'T CHANGE THE CODE BELOW
mary = Person("Mary", "Dylan", "Oct 12, 2002")
july = Person('July','Mccafee','Nov 12, 2002')
print(mary)
print(july)
