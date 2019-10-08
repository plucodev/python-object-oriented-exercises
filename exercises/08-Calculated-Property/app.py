class Person:
	# the constructor receives 3 params
    def __init__ (self) :
          self.brand = 'Epson'  # Will be a string
          self.model = 'TX-200' # Will be a string



    def get_age(self): # birthday is a date
        self.age_DifMs = Date.now() - self._birthday.getTime()
        age_Date = new Date(ageDifMs) # milliseconds from epoch
        return Math.abs(ageDate.getUTCFullYear() - 1970)


    def can_drinkAlcohol():
      #your code here
      let age = this.getAge()
      if(age >= 21){
        return true
      }
      else { return false; }

    }
}

let mario = new Person(2018, 10, 20)
print(mario.canDrinkAlcohol())