def get_top_items():
    print("Welcome to the Top 5 Items Social Media Platform!")
    user_name = input("Please enter your name: ")

    print("\nCategories: Movies, Books, Songs, Places, Foods, etc.")
    category = input("Choose a category for your top 5 items: ")

    top_items = []
    print(f"\nEnter your top 5 items in the category of {category}.")
    for i in range(5):
        item = input(f"Item {i+1}: ")
        top_items.append(item)

    print("\nYour Top 5 Items:")
    print(f"User: {user_name}")
    print(f"Category: {category}")
    for i, item in enumerate(top_items, start=1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    get_top_items()

# The Python program you're looking at is designed to simulate a very basic social media platform where users can share their top 5 favorite items in a specified category. Here's a breakdown of its components and functionality:

# Function Definition (get_top_items):

# The program defines a function named get_top_items, which encapsulates all the functionality of the application.
# Welcome Message:

# As soon as the function starts, it prints a welcome message to the user, introducing them to the "Top 5 Items Social Media Platform".
# User Name Input:

# The program prompts the user to enter their name using the input function. The entered name is stored in the variable user_name.
# Category Selection:

# The user is given a suggestion of categories (like Movies, Books, Songs, etc.) and is asked to choose one. The chosen category is stored in the variable category.
# Top 5 Items Input:

# The program then asks the user to enter their top 5 items in the chosen category.
# It uses a for loop that runs 5 times, each time prompting the user to enter an item.
# These items are appended to the list top_items.
# Displaying the Results:

# After the user has entered all their items, the program prints a formatted display of the user's name, the chosen category, and the list of top 5 items.
# It uses another for loop to enumerate and print each item in the top_items list.
# Main Block:

# The if __name__ == "__main__": line checks if the script is being run directly (not being imported as a module in another script).
# If the script is run directly, it calls the get_top_items function, initiating the program.
# This script is a console-based application and interacts with the user through text inputs and outputs. 
# It's a simple demonstration and doesn't include features like a graphical interface, data persistence, or networked communication, which would be necessary for a real-world social media application.