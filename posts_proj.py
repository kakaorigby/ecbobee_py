import requests
import random

JSONPlaceholder_API_URL = "https://jsonplaceholder.typicode.com/"

def get_random_posts(): 
    response = requests.get(f"{JSONPlaceholder_API_URL}/posts") # Will return 100 posts as per docs
    posts = response.json()
    random.shuffle(posts)  # Shuffle posts list
    return posts[:10]  # Return the first 10 posts after shuffling

def main():
    posts = get_random_posts()

    for i in range(len(posts)):
        print(f"{i+1}. {posts[i]['title']}")

if __name__ == "__main__":
    main()