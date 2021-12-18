# Classes : Something similar but powerful then functions.

def anything():
  print("An")


class Car:
  # Constructor : Takes in parameters for the class.
  def __init__(self,model,year):
    self.model = model
    self.year = year
  
  # def __str__():
  #   return "I am a Car class"


  # Methods
  def test(self):
    print(self.model)


newCar1 = Car('Limbo',2019)
newCar2 = Car('Porche',2020)