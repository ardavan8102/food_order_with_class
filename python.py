from colorama import Fore, init
init()

# Colors
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
purple = Fore.MAGENTA

# Text Styles
line_seprator = purple + "* * * * * * * * * * * * *" + white

# Main Food Class
class Food():
    def __init__(self, foodType):
        self.foodType = foodType


class Pizza(Food):
    def __init__(self, Type, size):
        super().__init__("Fast Foods")
        self.size = size

        if size.lower() == "big":
            self.size = "8 Slice"
        elif size.lower() == "small":
            self.size = "6 Slice"
        else:
            self.size = "6 Slice (By Default)"

        self.price = "150 T"
        self.Type = Type

class Kabab(Food):
    def __init__(self, Type, sikh):
        super().__init__("Rice Foods")
        self.sikh = sikh
        self.size = f"1 Boshqab Berenj & {self.sikh} Sikh Kabab"

        kabab_money = sikh * 30 # 30 T For Each Skewer
        rice_money = 110
        food_money = kabab_money + rice_money # Total Money

        self.price = str(food_money) + " T"
        self.Type = Type



food = ""

# Main Loop
while True:
    customer_welcome = input(red + "SYSTEM: " + yellow +"Welcome Dear, Do You Want Food? (y/n) " + white)

    # If User Decline Order Request :
    if customer_welcome == "n":
        print(line_seprator) # Line Seprator (* * * * * * * * * *)
        print(red + "SYSTEM: " + green + "See You Next Time ❤️")
        break

    # If User Accept Order Request :
    elif customer_welcome == "y": 

        print(line_seprator) # Line Sepator

        customer_food_type = input(red + "SYSTEM: " + yellow + "What Kind Of Food Do You Want? " + white)

        if customer_food_type.lower() == "pizza":
            
            print(line_seprator)
            pizza_kind = input(red + "SYSTEM: " + yellow + "What Kind Of Pizza You Want? " + white)

            print(line_seprator)
            pizza_size = input(red + "SYSTEM: " + yellow + "What Size Of Pizza You Want? " + white)

            food = Pizza(
                Type = pizza_kind, 
                size = pizza_size
            )

            print(line_seprator)

            print(red + "SYSTEM: " + green + f"Order Confirmed !\nFood Type : {food.Type}\nFood Price : {food.price}\nFood Size : {food.size}" + white)

            print(line_seprator)

        elif customer_food_type.lower() == "kabab":

            print(line_seprator)
            kabab_kind = input(red + "SYSTEM: " + yellow + "What Kind Of Kabab You Want? " + white)

            print(line_seprator)
            kabab_sikh = int(input(red + "SYSTEM: " + yellow + "How Many Skewers Of Kabab You Want? " + white))

            food = Kabab(
                Type = kabab_kind, 
                sikh = kabab_sikh
            )

            print(line_seprator)

            print(red + "SYSTEM: " + green + f"Order Confirmed !\nFood Type : {food.Type}\nFood Price : {food.price}\nSkewers : {food.sikh} Skewers Kabab" + white)

            print(line_seprator)

        else:
            print(red + "SYSTEM: " + green + "Unknow Type !" + white)
            print(red + "SYSTEM: " + green + "'Pizza' OR 'Kabab' As Food !" + white)
            continue

        
