import requests
import random

JSONPlaceholder_API_URL = "https://jsonplaceholder.typicode.com/"

def get_random_posts(): 
    response = requests.get(f"{JSONPlaceholder_API_URL}/posts") # Will return 100 posts as per docs
    posts = response.json()
    random.shuffle(posts)  # Shuffle posts list
    return posts[:10]  # Return the first 10 posts after shuffling


def main():
    print("This is the JSON Posts Project.")
    print("Here is a list 10 random posts:")

    posts = get_random_posts()
    for i in range(len(posts)):
        print(f"{i+1}. {posts[i]['title']}")

    invalid = True
    while(invalid):
        print("\nWhich Post would you like to view? (Choose from 1-10)")
        choice = int(input("Enter your choice: "))
        if (choice < 11 and choice > 0):
            invalid = False
        else:
            print("Please choose within the bounds 1-10!")
    trueIndex = choice - 1

if __name__ == "__main__":
    main()