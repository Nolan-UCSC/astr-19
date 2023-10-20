#Have the data members of the class represent the following physical parameters of the anima
class FavoriteAnimal:
    def __init__(self, length_of_the_arms, length_of_the_legs, number_of_eyes, does_it_have_a_tail, is_it_furry):
        self.length_of_the_arms = length_of_the_arms
        self.length_of_the_legs = length_of_the_legs
        self.number_of_eyes = number_of_eyes
        self.does_it_have_a_tail = does_it_have_a_tail
        self.is_it_furry = is_it_furry

#ollowing physical parameters of the animal:
    # length of the arms (float),
    # length of the legs (float),
    # number of eyes (int),
    # does it have a tail? (bool),
    # is it furry? (bool).

    def describe(self):
        print(f"Physical Characteristics of My Favorite Animal:")
        print(f"length of the arms : {self.length_of_the_arms} m")
        print(f"length of the legs: {self.length_of_the_legs} m")
        print(f"number of eyes: {self.number_of_eyes}")
        if self.does_it_have_a_tail:
            print("does it have a tail: Yes")
        else:
            print("does it have a tail: No")
        if self.is_it_furry:
            print("is it furry?: Yes")
        else:
            print("is is furry: No")

# Create an instance of the FavoriteAnimal class
# I googled an aligators stats its not my fav but the first that came ti mind
my_favorite_animal = FavoriteAnimal(4.5, 4.5, 2, True, False)

# call function
#Write a member function of the class to print out and describe the data members
# representing the physical characteristics of the animal.
my_favorite_animal.describe()
