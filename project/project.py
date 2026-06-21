def suggest_by_height(height):
    #Suggest a flower based on height preference
    if height == 'tall':
        return 'Sunfalower'
    elif height == 'medium':
        return 'Rose'
    elif height == 'short':
        return 'Daisy'
    else:
        return 'Unknown height preference'

def suggest_by_smell(smell):
    #Suggest a flower based on smell preference
    if smell == 'strong':
        return 'Jasmine'
    elif smell == 'mild':
        return 'Lavendar'
    elif smell == 'none':
        return 'Cactus'
    else:
        return 'Unknown smell preference'

def suggest_by_color(color):
    #Suggest a flower based on color preference
   if color == 'red':
       return 'Rose'
   elif color == 'yellow':
       return 'Sunflower'
   elif color == 'white':
        return 'Lily'
   else:
        return 'Unknown color prefernce'

def main():
    #main function to interact with the user and provide flower suggestions
    print("Welcome to the Flower Suggestion Program!")

    #Collect user preferences
    height = input("Choose height (tall, medium, short): ").lower()
    smell = input("Choose smell(strong, mild, none): ").lower()
    color = input("Choose color (red, yellow, white): ").lower()

    #Get suggestions based on preferences
    flower_by_height = suggest_by_height(height)
    flower_by_smell = suggest_by_smell(smell)
    flower_by_color = suggest_by_color(color)

    #Display suggestions
    print(f"Based on height, we suggest: {flower_by_height}")
    print(f"Based on smell, we suggest: {flower_by_smell}")
    print(f"Based on color, we suggest: {flower_by_color}")

if __name__ == "__main__":
    main()

