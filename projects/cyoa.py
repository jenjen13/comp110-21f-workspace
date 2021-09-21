"""Cooking mama simulator!"""

from random import randint
points: int = 0
player: str = input("Hello! Before we get started, what is your name? ")
WINKING: str = "\U0001F609"
FIRE: str = "\U0001F525"
DROP: str = "\U0001F4A7"
SAD_EMOJI: str = "\U0001F61E"
SMILE_EMOJI: str = "\U0001F60A"
number: int = (randint(1, 100))
DON: str = "\U0001F369"
CAKE: str = "\U0001F382"
PIE: str = "\U0001F967"
SPARKLE: str = "\U00002728"
HEART: str = "\U00002764\U0000FE0F"


def main() -> None:
    """The program's entrypoint."""
    greet()
    intro()
    print(f"{player} currently has: {points} points")
    print(f"Thank you for playing Cooking Mama {player}! Come Again Next Time {HEART}")


def greet() -> None:
    """Greet player."""
    print(f"{SPARKLE} Greetings {player}! {SPARKLE} Welcome to Cooking Mama!\nToday is a very busy day so we must get started quickly!")
    print("Sadly, I have lost my cookbook, so I am going to need your help with the recipe.")
    print(f"{SPARKLE} (If your recipe is right, you will have a higher number of points. If you add the wrong amount of ingredients together, your points will be deducted) {SPARKLE}")
    print("Fortunately, you have many choices today! We can make a cake for a special guest, a donut for a friend, a pie for grandma, or a mystery game.")
    print(f"{CAKE} {DON} {PIE}")


def intro() -> None:
    """Intro."""
    choice: str = input(f"{SPARKLE} What will you choose today? Cake, donut, pie, mystery game, or end the game: ")
    global points
    points = points - points
    if choice == str("pie"):
        pie()
    else: 
        if choice == str("cake"):
            cake()
        else:
            if choice == str("donut"):
                donut()
            else:
                if choice == str("mystery game" or "a mystery game" or "mystery"):
                    mystery(points)


def cont() -> None:
    """Continue or end."""
    print("Would you like to continue the game?")
    contin: str = input("Type \"Yes\" to continue the game or \"No\" to end the game: ")
    if contin == str("yes" or "Yes"):
        intro()


def mystery(points: int) -> int:
    """Entry point to game."""
    print(f"Welcome to the mystery game {player}! Today we're going to play a guessing game!")
    print(f"All the donuts that we make today have a random number of sprinkles on them from 1 to 100. {DON}{DON}{DON}") 
    print("You're job will be to guess the number of sprinkles there are on each donut. If you guess incorrectly, your number of points will be deducted.")
    print("Let's begin!")
    game()
    return points


def game() -> None:
    """The game."""
    global number
    global points
    guess: int = int(input("The donut has __ number of sprinkles: "))
    if guess == number:
        points = points + guess
        print(f"{player} has: {points} points {SPARKLE}")
        cont()
    else:
        points = points - guess
        print(f"{player} has: {points} points {SAD_EMOJI}")
        cont()


def pie() -> None:
    """Pie Route."""
    global points
    print(f"{player} currently has: {points} points")
    print(f"Yay we will be making a pie for grandma today! I love a warm pie! \nToday we will be making a apple pie that will make grandma love you even more! {PIE}")
    print("First, we need to get the ingredients. (hint: whole numbers only!!)")
    apple: int = int(input("How many apples do we need? "))
    if apple == 6:
        points = points + 6
    else:
        points = points - apple
    sugar: int = int(input("How many cups of sugar do we need? "))
    if sugar == 1:
        points = points + 1
    else:
        points = points - sugar
    butter: int = int(input("How many sticks of butter do we need? "))
    if butter == 1:
        points = points + 1
    else:
        points = points - butter
    pie_crust: int = int(input(f"How many pie crusts do we need? (hint: we only need 1 {WINKING}): "))
    if pie_crust == 1:
        points = points + 1
    else:
        points = points - 1
    print("Perfect! Next we need to mix!")
    mix: str = str(input("Type the word “mix” to mix the apples, sugar, and additional spice together: "))
    print(f"Let's {mix}!")
    points = points + 1
    degree: int = int(input("Great! While I put the filling in the pie and add the top crust, what temperature should the oven be at? (hint: numbers only!): "))
    if degree == 425:
        points = points + 425
    else:
        points = points - degree
    print("Okay!")
    minute: int = int(input("Yay! Almost there! Now while I put the pie in the oven, how many minutes should we bake the pie for? "))
    if minute == 45:
        points = points + minute
    else:
        points = points - minute
    print("Perfect!")
    print("*ding*")
    if apple == 6 and sugar == 1 and butter == 1 and pie_crust == 1 and degree == 425 and minute == 45:
        print("The pie is done! Hooray! We made a perfect apple pie! Grandma will love this!")
    else:
        if apple == 6 and sugar == 1 and butter == 1 and pie_crust == 1 and 425 > degree and 45 > minute:
            print("The pie is done! Hooray! We made a great apple pie, although it might be a little undercooked! \nGrandma will still love this pie because you made it!")
        else:
            if apple > 6 and sugar > 1 and butter > 1 and pie_crust > 1 and 425 > degree and 45 > minute:
                print("The pie is done! Hooray! We made a great apple pie, although it might be a little undercooked! \nGrandma will still love this pie because you made it!")
            else:
                if apple > 6 and sugar > 1 and butter > 1 and pie_crust > 1 and degree == 425 and minute == 45:
                    print("The pie is done! Hooray! We made a great apple pie, although it might taste a little funky! \nGrandma will still love this pie because you made it!")
                else:
                    if apple < 6 and sugar < 1 and butter < 1 and pie_crust < 1 and degree == 425 and minute == 45:
                        print("The pie is done! Hooray! We made a great apple pie, although it might taste a little funky! \nGrandma will still love this pie because you made it!")
                    else:
                        if apple < 6 and sugar < 1 and butter < 1 and pie_crust < 1 and 425 > degree and 45 > minute:
                            print("The pie is done! Hooray! We made a great apple pie, although it might taste a little funky! \nGrandma will still love this pie because you made it!")
                        else:
                            burning()
    print("Yay you have given grandma your pie! Now let's see how many points you have received.")
    print(f"{player} currently has: {points} points")
    if points == 480:
        print(f"{SPARKLE} Yay you have made the perfect pie! Congratulations!! {SPARKLE}")
        print(PIE)
    else: 
        print(f"On no {SAD_EMOJI} You didn't make the recipe exactly and something went wrong.")
        print("I think I have the recipe saved somewhere. Hold on let me look.")
        print(f"A-ha! I found it. {SPARKLE} \nThe recipe for the pie cake is: \napples: 6 \nsugar: 1 \nbutter: 1 \npie crust: 1 \ndegree: 425 \nminute: 45")
        print(f"Make sure you write the recipe down so next time your score can be higher {SMILE_EMOJI}")
    return cont()


def burning() -> None:
    """The pie is burnt."""
    print("Oh no! The amount of time was wrong and now the pie is burning!")
    print(f"The oven is on fire!!! {FIRE} {FIRE} {FIRE} {FIRE} \nQuickly we must put the fire out! ")
    water: str = str(input("Type “water” to spray water into the oven: "))
    print(f"Spraying {water}.")
    global points
    points = points + 1
    print("Oh no it's not helping! You need to call 911 for help.")
    emergency: str = str(input("Type “911” to call the fire department: "))
    print(f"Calling {emergency}.")
    points = points + 1
    print("*siren noises*")
    print(f"{FIRE} {FIRE} {FIRE}")
    print(f"{FIRE} {FIRE} {DROP}")
    print(f"{FIRE} {DROP} {DROP}")
    print(f"{DROP} {DROP} {DROP}")
    print("*Whew* Thanks to the firemen, the fire was put out. But sadly, the pie got burnt.")
    print("Grandma will still appreciate that you attempted to make her a pie.")


def cake() -> None:
    """Cake route."""
    global points
    print(f"Hooray! I love making cake! \nWe will be making a vanilla cake with strawberries on top of it. {CAKE}")
    print(f"{player} currently has: {points} points")
    print("First, we need to get the ingredients. (hint: whole numbers only!!)")
    sugar: int = int(input("How many cups of sugar do we need? "))
    if sugar == 1:
        points = points + 1
    else:
        points = points - sugar
    eggs: int = int(input("How many eggs do we need? "))
    if eggs == 2:
        points = points + 2
    else:
        points = points - eggs
    flour: int = int(input("How many cups of flour do we need? "))
    if flour == 2:
        points = points + 2
    else:
        points = points - flour
    butter: int = int(input("How many sticks of butter do we need? "))
    if butter == 1:
        points = points + 1
    else:
        points = points - butter
    milk: int = int(input("How many cups of milk do we need? "))
    if milk == 1:
        points = points + 1
    else:
        points = points - milk
    strawberries: int = int(input("How many strawberries do we need? "))
    if strawberries == 6:
        points = points + 6
    else:
        points = points - strawberries
    mix: str = str(input("Perfect! Next we need to mix! Type the word \"mix\" to mix the batter together: "))
    print(f"Let's {mix}!")
    points = points + 1
    degree: int = int(input("Great! While I grease the cake pan, what temperature should the oven be at? (hint: numbers only!): "))
    if degree == 350:
        points = points + 350
    else:
        points = points - degree
    minute: int = int(input("Yay! Almost there! Now while I pour the batter into the pan and put the cake in the oven, how many minutes should we bake the cake for? "))
    if minute == 35:
        points = points + 35
    else:
        points = points - minute
    print("Perfect! \n*ding*")
    print("Now we need to put icing on the cake and add the strawberries.")
    ingred: str = str(input("Type \"berries and cream\" to add the final ingredients on the cake: "))
    print(f"Adding {ingred}.")
    points = points + 1
    print("Good job! You iced the cake and added the strawberries perfectly!")
    if sugar == 1 and eggs == 2 and flour == 2 and butter == 1 and milk == 1 and strawberries == 6 and degree == 350 and minute == 35:
        print(mary())
    else:
        if sugar == 1 and eggs == 2 and flour == 2 and butter == 1 and milk == 1 and strawberries == 6 and degree < 350 or minute < 35:
            print(gordon_one())
        else:
            if sugar > 1 and eggs > 2 and flour > 2 and butter > 1 and milk > 1 and strawberries > 6 and degree == 350 and minute == 35:
                print(gordon_two())
            else:
                if 1 > sugar and 2 > eggs and 2 > flour and 1 > butter and 1 > milk and 6 > strawberries and degree < 350 and minute < 35:
                    print(gordon_two())
                else:
                    if sugar < 1 and eggs < 2 and flour < 2 and butter < 1 and milk < 1 and strawberries < 6 and degree == 350 and minute == 35:
                        print(gordon_three())
                    else: 
                        if sugar < 1 and eggs < 2 and flour < 2 and butter < 1 and milk < 1 and strawberries < 6 and degree < 350 and minute < 35:
                            print(gordon_three())
                        else:
                            print(gordon_four())
    print("Yay you have fed your guest! Now let's see how many points you have received.")
    print(f"{player} currently has: {points} points")
    if points == 403:
        print(f"{SPARKLE} Yay you have made the perfect cake! Congratulations!! {SPARKLE}")
        print(f"{CAKE}")
    else: 
        print(f"On no {SAD_EMOJI} You didn't make the recipe exactly and something went wrong.")
        print("I think I have the recipe saved somewhere. Hold on let me look.")
        print(f"A-ha! I found it. {SPARKLE} \nThe recipe for the perfect cake is: \nsugar: 1 \neggs: 2 \nflour: 2 \nbutter: 1 \nmilk: 1 \nstrawberries: 6 \ndegree: 350 \nminute: 35")
        print(f"Make sure you write the recipe down so next time your score can be higher {SMILE_EMOJI}")
    return cont()


def mary() -> None:
    """Mary encourages you."""
    print("Yay! The cake came out perfect! Now let’s give the cake to our special guest!")
    print("Introducing Mary Berry from the Great British Bake Off! Welcome Mary!")
    expression: str = str(input("Type “smile nervously” to make an expression at the sight of Mary Berry: "))
    print(f"You {expression}.")
    global points
    points = points + 1
    print("Mary looks at your cake in delight.")
    print("She says \"Your cake tastes absolutely enchanting! I love the way strawberries were added to compliment the sweetness of the cake. Your icing is not too sweet which adds a nice touch\"")
    smile: str = str(input("Type “smile brightly” to respond to the compliment: "))
    print(f"You {smile}.")
    points = points + 1
    thanks: str = str(input("Type “Thank You Mary!” to respond back to Mary: "))
    print(f"You say {thanks}.")
    points = points + 1


def gordon_one() -> None:
    """Gordon yells at you first option."""
    print("Yay! We made a great cake, even if it is a little undercooked hehe. Now let’s give the cake to our special guest!")
    print("Introducing Gordon Ramsay! Welcome Gordon!")
    nervous: str = str(input("Type “smile nervously” to make an expression at the sight of Gordon Ramsey: "))
    print(f"You {nervous}.")
    global points
    points = points - 1
    print("Gordon looks at your cake in disdain.")
    print("He says \"For what we are about to eat, may the Lord make us truly not vomit\" \nGordon tries your cake.")
    print("He says \"Your cake is not good. Not good at all. Your cake is lumpy and… is this an eggshell? Try again next time.\"")
    sad: str = str(input("Type “sad” to express your feelings: "))
    print(f"You look {sad}.")
    points = points - 1
    print("Gordon shakes his head in disappointment at your cake.")
    response: str = str(input("Type “Yes chef” to respond to Gordon Ramsay: "))
    print(f"You say {response}.")
    points = points + 1


def gordon_two() -> None:
    """Gordon yells at you second option."""
    print("Yay! We made a great cake, even if the recipe is a little off hehe. Now let’s give the cake to our special guest!")
    print("Introducing Gordon Ramsay! Welcome Gordon!")
    nervous: str = str(input("Type “smile nervously” to make an expression at the sight of Gordon Ramsey: "))
    print(f"You {nervous}.")
    global points
    points = points - 1
    print("Gordon looks at your cake in disdain.")
    print("He says \"For what we are about to eat, may the Lord make us truly not vomit\" \nGordon tries your cake.")
    print("He says \"Your cake is not good. Not good at all. Your cake is lumpy and your frosting is thin. Try again next time.\"")
    sad: str = str(input("Type “sad” to express your feelings: "))
    print(f"You look {sad}.")
    points = points - 1
    print("Gordon shakes his head in disappointment at your cake.")
    response: str = str(input("Type “Yes chef” to respond to Gordon Ramsay: "))
    print(f"You say {response}.")
    points = points + 1


def gordon_three() -> None:
    """Gordon yells at you third option."""
    print("Yay! We made a great cake, even if it is a little undercooked hehe. Now let’s give the cake to our special guest!")
    print("Introducing Gordon Ramsay! Welcome Gordon!")
    nervous: str = str(input("Type “smile nervously” to make an expression at the sight of Gordon Ramsey: "))
    print(f"You {nervous}.")
    global points
    points = points - 1
    print("Gordon looks at your cake in disdain.")
    print("He says \"For what we are about to eat, may the Lord make us truly not vomit\" \nGordon tries your cake.")
    print("He says \"Your cake is not good. Not good at all. You haven’t cooked your cake and it is covered in thick icing. Try again next time.\"")
    sad: str = str(input("Type “sad” to express your feelings: "))
    print(f"You look {sad}.")
    points = points - 1
    print("Gordon shakes his head in disappointment at your cake.")
    response: str = str(input("Type “Yes chef” to respond to Gordon Ramsay: "))
    print(f"You say {response}.")
    points = points + 1


def gordon_four() -> None:
    """Gordon yells at you fourth option."""
    print("Yay! We made a great cake, even if the recipe and cooking timing is a little off hehe. Now let’s give the cake to our special guest!")
    print("Introducing Gordon Ramsay! Welcome Gordon!")
    nervous: str = str(input("Type “smile nervously” to make an expression at the sight of Gordon Ramsey: "))
    print(f"You {nervous}.")
    global points
    points = points - 1
    print("Gordon is offended at the sight of your cake.")
    print("He says \"Your cake is absolutely disgusting. You have somehow messed up the recipe completely and burnt the entire cake. You absolute donkey. My gran could do better! And she’s dead.\"")
    fear: str = str(input("Type “shaking in fear” to express your feelings: "))
    print(f"You are {fear}.")
    points = points - 1
    print("Gordon frowns at your cake.")
    response: str = str(input("Type “Yes chef” to respond to Gordon Ramsay: "))
    print(f"You say {response}.")
    points = points + 1


def donut() -> None:
    """Donut Route."""
    global points
    print("Good choice! Donuts are so yummy!!!! \nWe will be making chocolate covered donuts today!")
    print(f"{player} currently has: {points} points")
    print(f"{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}")
    print("First, we need to get the ingredients. (hint: whole numbers only!!)")
    sugar: int = int(input("How many cups of sugar do we need? "))
    if sugar == 1:
        points = points + 1
    else:
        points = points - sugar
    egg: int = int(input("How many eggs do we need? "))
    if egg == 2:
        points = points + 2
    else:
        points = points - egg
    flour: int = int(input("How many cups of flour do we need? "))
    if flour == 3:
        points = points + 3
    else:
        points = points - flour
    butter: int = int(input("How many sticks of butter do we need? "))
    if butter == 2:
        points = points + 2
    else:
        points = points - butter
    milk: int = int(input("How many cups of milk do we need? "))
    if milk == 1:
        points = points + 1
    else:
        points = points - milk
    print("Perfect! Next we need to mix!")
    mix: str = str(input("Type the word “mix” to mix dough together: "))
    print(f"Let's {mix}!")
    points = points + 1
    minute: int = int(input("Great! Now while I knead and roll out the dough, how many minutes should we fry each donut? "))
    if minute == 2:
        points = points + 2
    else:
        points = points - minute
    print("Okay!")
    print("*frying noises*")
    icing: str = str(input("The donuts are done! Next we need to put icing on the donuts and put sprinkles on them. Type \"add\" to add icing and sprinkles: "))
    print(f"Adding {icing}.")
    points = points + 1
    print(f"{SPARKLE} Perfect! You iced the donuts and added {number} of sprinkles on each donut.")
    if sugar == 1 and egg == 2 and flour == 3 and butter == 2 and milk == 1 and minute == 2:
        print(f"Yay! We made 12 chocolate covered donuts and they turned out perfect Your friend will appreciate you making donuts for them {HEART}")
    else:
        if sugar == 1 and egg == 2 and flour == 3 and butter == 2 and milk == 1 and minute < 2:
            print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little undercooked. But it's okay! Your friend will appreciate you making donuts for them {HEART}")
        else:
            if 1 < sugar or 2 < egg or 3 < flour or 2 < butter or 1 < milk and minute < 2:
                print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little lumpy and undercooked. But it's okay! Your friend will appreciate you making donuts for them {HEART}")
            else:
                if 1 < sugar or 2 < egg or 3 < flour or 2 < butter or 1 < milk and minute == 2:
                    print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little lumpy. But, it’s okay! Your friend will appreciate you making donuts for them {HEART}")
                else:
                    if 1 > sugar or 2 > egg or 3 > flour or 2 > butter or 1 > milk and minute == 2:
                        print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little lumpy. But it's okay! Your friend will appreciate you making donuts for them {HEART}")
                    else:
                        if 1 > sugar or 2 > egg or 3 > flour or 2 > butter or 1 > milk and 2 > minute:
                            print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little lumpy and underboocked. But, it’s okay! Your friend will appreciate you making donuts for them {HEART}")
                        else:
                            print(f"Yay! We made 12 chocolate covered donuts, but they turned out a little lumpy and burnt. But, it’s okay! Your friend will appreciate you making donuts for them {HEART}")
    print("Yay you have given your friend the donuts! Now let's see how many points you have received.")
    print(f"{player} currently has: {points} points")
    if points == 13:
        print(f"{SPARKLE} Yay you have made perfect donuts! Congratulations!! {SPARKLE}")
        print(f"{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}{DON}")
    else: 
        print(f"On no {SAD_EMOJI} You didn't make the recipe exactly and something went wrong.")
        print("I think I have the recipe saved somewhere. Hold on let me look.")
        print(f"A-ha! I found it. {SPARKLE} \nThe recipe for the perfect donuts is: \nsugar: 1 \negg: 2 \nflour: 1 \nbutter: 1 \nmilk: 1 \nminute: 2")
        print(f"Make sure you write the recipe down so next time your score can be higher! {SMILE_EMOJI}")


if __name__ == "__main__":
    main()