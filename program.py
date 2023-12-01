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