
def makingSmallList(): # THIS IS GOOD
    ingredientInput = input("Ingredient: ").lower()
    unitInput = input("Unit: ")
    quantityInput = input("Quantity: ").lower()

    while type(quantityInput) == str:
        try:
            quantityInput = round(float(quantityInput), 2)
            if (quantityInput <= 0):
                quantityInput = input("Invalid Input. Quantity: ").lower()
        except:
            quantityInput = input("Invalid Input. Quantity: ").lower()

    return [ingredientInput, unitInput, quantityInput]

def unitValidity(unit):
    global validUnitsList


# procedure converting units
# procedure for scaling


ingredientBigList = []
programStatus = True
# START OF CODE ------------------------------------------------
while programStatus == True:
    ingredientBigList.append(makingSmallList())
    nextIngredient = None
    while nextIngredient not in ["y", "yes", "n", "no"]:
        nextIngredient = (input("Input another item?\n y/n ")).lower()
    if nextIngredient in ["y", "yes"]:
        continue
    elif nextIngredient in ["n", "no"]:
        programStatus = False



for ingredient in ingredientBigList:
    print(f"{ingredient[2]} {ingredient[1]} of {ingredient[0]}")


#do math stuff calculate stuff (love ✨✨✨)




#print result




##################


# Volume Units
validUnitsList = [ #PLZ CHECK THIS LIST AGAINST SOMETHING PLZPLZPLZ
    "teaspoon", "teaspoons", "tsp",
    "tablespoon", "tbsp",
    "fluid ounce", "fl oz",
    "cup", "cups", "c",
    "pint", "pints", "pt",
    "quart", "quarts", "qt",
    "gallon", "gallons", "gal",
    "milliliter", "milliliters", "mL",
    "liter", "liters", "L",
    "dash", "dashes",
    "pinch", "pinches",
    "drop", "drops",
    "ounce", "ounces", "oz",
    "pound", "pounds", "lb", "lbs",
    "milligram", "milligrams", "mg",
    "gram", "grams", "g",
    "kilogram", "kilograms", "kg",
    "stick", "sticks",
    "bunch", "bunches",
    "clove", "cloves"
]
