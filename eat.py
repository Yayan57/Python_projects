day = input("What day is it?")
day = day.lower()
wantMeat = input("Do you want meat? (Y/N)")
wantMeat = wantMeat.lower()

def meat(meat):
    if whatMeat == "beef":
        if day == "monday":
            return "Eat a salad"
        if day == "tuesday":
            return "Eat a Hummus Veggie Wrap"
        if day == "wednesday":
            return "Eat some Curry Lentil Soup"
        if day == "thursday":
            return "eat a salad"
        if day == "friday":
            return "eat a salad"
        if day == "saturday":
            return "eat a salad"
        if day == "sunday":
            return "eat a salad"
        else:
            return "its a cheat day :) eat a single oreo today :)))))))"
        if whatMeat == "chicken":
            if day == "monday":
                return "Eat a salad"
            if day == "tuesday":
                return "Eat a Hummus Veggie Wrap"
            if day == "wednesday":
                return "Eat some Curry Lentil Soup"
            if day == "thursday":
                return "eat a salad"
            if day == "friday":
                return "eat a salad"
            if day == "saturday":
                return "eat a salad"
            if day == "sunday":
                return "eat a salad"
            else:
                return "its a cheat day :) eat a single oreo today :)))))))"
        if whatMeat == "pork":
            if day == "monday":
                return "Eat a salad"
            if day == "tuesday":
                return "Eat a Hummus Veggie Wrap"
            if day == "wednesday":
                return "Eat some Curry Lentil Soup"
            if day == "thursday":
                return "eat a salad"
            if day == "friday":
                return "eat a salad"
            if day == "saturday":
                return "eat a salad"
            if day == "sunday":
                return "eat a salad"
            else:
                return "its a cheat day :) eat a single oreo today :)))))))"
        if whatMeat == "seafood":
            if day == "monday":
                return "Eat a salad"
            if day == "tuesday":
                return "Eat a Hummus Veggie Wrap"
            if day == "wednesday":
                return "Eat some Curry Lentil Soup"
            if day == "thursday":
                return "eat a salad"
            if day == "friday":
                return "eat a salad"
            if day == "saturday":
                return "eat a salad"
            if day == "sunday":
                return "eat a salad"
            else:
                return "its a cheat day :) eat a single oreo today :)))))))"




def veggies(day_of_the_week):
    if day == "monday":
       return "Eat a salad"
    if day == "tuesday":
        return "Eat a Hummus Veggie Wrap"
    if day == "wednesday":
        return "Eat some Curry Lentil Soup"
    if day == "thursday":
        return "eat a salad"
    if day == "friday":
        return "eat a salad"
    if day == "saturday":
        return "eat a salad"
    if day == "sunday":
        return "eat a salad"
    else:
        return "its a cheat day :) eat a single oreo today :)))))))"



if wantMeat == "y":
    whatMeat = input("what kind of meat do you want?")

if wantMeat == "n":
    vegetarianMeal = veggies(day)

    print(vegetarianMeal)



