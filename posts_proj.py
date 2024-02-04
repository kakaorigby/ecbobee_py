import requests
import random
from profanity_check import predict, predict_prob

JSONPlaceholder_API_URL = "https://jsonplaceholder.typicode.com/"

# ANSI escape code for bold text
BOLD = "\033[1m"
# ANSI escape code to reset text formatting
RESET = "\033[0m"


def print_bold(text):
    print(f"{BOLD}{text}{RESET}")


def get_random_posts():
    # Will return 100 posts as per docs
    response = requests.get(f"{JSONPlaceholder_API_URL}/posts")
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
    response = requests.get(
        f"{JSONPlaceholder_API_URL}/posts/{post_id}/comments")
    comments = response.json()
    for comment in comments:
        print(f"\n{comment['name']}:{comment['body']}")


def publish_comment(post_id, text_input, name, email):
    comment_data = {
        'postId': post_id,
        'name': name,
        'email': email,
        'body': text_input
    }
    # NOTE this is just a test site, not actually POSTing this data as per docs
    response = requests.post(
        f"{JSONPlaceholder_API_URL}/comments", json=comment_data)
    if (response.status_code == 201):
        print("\nComment published successfully!")
    else:
        print("\nFailed to publish comment.")


def main():
    print("This is the JSON Posts Project.")
    print("Here is a list 10 random posts:")

    posts = get_random_posts()
    for i in range(len(posts)):
        # i+1 to ensure user-facing index is 1 to 10
        print(f"{i+1}. {posts[i]['title']}")

    invalid = True
    while (invalid):
        print("\nWhich Post would you like to view? (Choose from 1-10)")
        choice = int(input("Enter your choice: "))
        if (choice < 11 and choice > 0):
            invalid = False
        else:
            print("Please choose within the bounds 1-10!")
    trueIndex = choice - 1  # Converts user-facing index to zero-based numbering

    print_specific_post(posts[trueIndex]['id'])
    invalid = True
    while (invalid):
        comments_choice = input(
            "Would you like to view the comments? Type \"YES\" or \"NO\": ")
        if (comments_choice.lower() == "yes" or comments_choice.lower() == "no"):
            invalid = False
            if (comments_choice.lower() == "yes"):
                print_post_comments(posts[trueIndex]['id'])
        else:
            print("Please type \"YES\" or \"NO\" ONLY")
    profanity = True
    while(profanity):
        comment_to_publish = input(
            "\nType your own comment now, or just press ENTER to skip: ")
        if (predict([comment_to_publish])):
            print("Please do not use profanity!")
        else:
            profanity = False

    if (comment_to_publish != ""):
        invalid = True
        while (invalid):
            name = input("\nEnter your name: ")
            email = input("also, enter your email: ")
            if (name != "" and email != ""):
                invalid = False
            else:
                print("Name and Email must not be blank!")

        publish_comment(posts[trueIndex]['id'],
                        comment_to_publish, name, email)


if __name__ == "__main__":
    main()
