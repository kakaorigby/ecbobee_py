import requests
import random

JSONPlaceholder_API_URL = "https://jsonplaceholder.typicode.com/"

# ANSI escape code for bold text
BOLD = "\033[1m"
# ANSI escape code to reset text formatting
RESET = "\033[0m"

def print_bold(text):
    print(f"{BOLD}{text}{RESET}")

def get_random_posts(): 
    response = requests.get(f"{JSONPlaceholder_API_URL}/posts") # Will return 100 posts as per docs
    posts = response.json()
    random.shuffle(posts)  # Shuffle posts list
    return posts[:10]  # Return the first 10 posts after shuffling

def print_specific_post(post_id):
    post = requests.get(f"{JSONPlaceholder_API_URL}/posts/{post_id}").json()
    print_bold("\nPost:")
    print(f"{post['title']}\n")
    print_bold("Body:")
    print(f"{post['body']}\n")

def print_post_comments(post_id):
    response = requests.get(f"{JSONPlaceholder_API_URL}/posts/{post_id}/comments")
    comments = response.json()
    for comment in comments:
        print(f"\n{comment['name']}:{comment['body']}")


def main():
    print("This is the JSON Posts Project.")
    print("Here is a list 10 random posts:")

    posts = get_random_posts()
    for i in range(len(posts)):
        print(f"{i+1}. {posts[i]['title']}") # i+1 to ensure user-facing index is 1 to 10

    invalid = True
    while(invalid):
        print("\nWhich Post would you like to view? (Choose from 1-10)")
        choice = int(input("Enter your choice: "))
        if (choice < 11 and choice > 0):
            invalid = False
        else:
            print("Please choose within the bounds 1-10!")
    trueIndex = choice - 1 # Converts user-facing index to zero-based numbering
    
    print_specific_post(posts[trueIndex]['id'])
    invalid = True
    while(invalid):
        comments_choice = input("Would you like to view the comments? Type \"YES\" or \"NO\": ")
        if(comments_choice.lower() == "yes" or comments_choice.lower() == "no"): 
            invalid = False
            if(comments_choice.lower() == "yes"):
                print_post_comments(posts[trueIndex]['id'])
        else:
            print("Please type \"YES\" or \"NO\" ONLY")

if __name__ == "__main__":
    main()