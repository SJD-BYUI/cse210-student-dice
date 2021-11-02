import random

# TODO: Define the Thrower class here.

class Thrower:
   """
   this class we will make the thrower or rather the things need from rolling the dice and the game play. 

   attributes
    - throw_dice I think this gets a new set of dice
    - dice is the set of dice that was just rolled
    - get_points this gets the points from that roll of the dice
    - can_throw decides if user is able to continue with the game
   """ 

   def __init__(self):
       """
       I think I need to create one of these but honestly I'm not 100% sure

       attributes -
        - throw_dice - gets a new roll of dice
        - get_points - the result of the last throw of dice
        - can_continue - determins if there are any ones or fives within the roll
       """

       self.dice = []



   def throw_dice(self):
       """
       this is to get a new set of dice that 
       """

       for _ in range(5):
           self.dice.append(random.randint(1,6))
    
   def get_points(self):
        points = 0

        for roll in self.dice:
            if roll == 1:
                points += 100
            elif roll == 5:
                points += 50
        
        return points

   def can_throw(self):
       points = self.get_points()

       self.dice=[]

       if points > 0:
           return True
       elif points == 0:
           return False


    



       
