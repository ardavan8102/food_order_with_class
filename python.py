from colorama import Fore, init
init()

# Main Food Class
class Food():
    def __init__(self, foodType):
        self.foodType = foodType


class Pizza(Food):
    def __init__(self, Type, size):
        super().__init__("Fast Food")
        self.size = size

        if size == "big":
            self.size = "8 Slice"
        elif size == "small":
            self.size = "6 Slice"
        else:
            self.size = "6 Slice (By Default)"

        self.price = "245 T"
        self.Type = Type

class Kabab(Food):
    def __init__(self, Type, sikh):
        super().__init__("Kabab & Joojeh")
        self.sikh = sikh
        self.size = f"1 Boshqab Berenj & {self.sikh} Sikh Kabab"
        self.price = "325 T"
        self.Type = Type


# Food Variables
food1 = Pizza(
    Type = "Peperoni",
    size = "small"
)

food2 = Kabab(
    Type = "Koobideh", 
    sikh = 3
)


# Colors
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE


print(red + "* * * * * * * * * * * * *" + white)

print(
    yellow + "Food : " + green + f"{food1.Type} Pizza \n" + yellow + "Gheymat :" + green + f" {food1.price}\n" + yellow + "Size Pizza :" + green + f" {food1.size}\n" + yellow + "Category : " + green + f"{food1.foodType}" + white
)

print(red + "* * * * * * * * * * * * *" + white)

print(
    yellow + "Food : " + green + f"{food2.Type} Kabab \n" + yellow + "Gheymat : " + green + f"{food2.price} \n" + yellow + "Shamele : " + green + f"{food2.size}\n" + yellow + "Category : " + green + f"{food2.foodType}" + white
)

print(red + "* * * * * * * * * * * * *" + white)