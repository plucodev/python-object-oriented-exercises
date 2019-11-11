class Person:
    def __repr__(self):
        return '{Name:'+' '+self.name+', Last Name:'+' '+str(self.last_name)+', Birth Date:' +' '+ str(self.birth_date) +'}'
    def __init__ (self,e,r,t) :
        self.name = e
        self.last_name = r
        self.birth_date = t
mary = Person("Mary", "Dylan", "Oct 12, 2002")
july = Person('July','Mccafee','Nov 12, 2002')
print(mary)
print(july)
