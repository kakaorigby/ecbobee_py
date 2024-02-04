# JSON Posts Project

This project interacts with the JSONPlaceholder API to retrieve random posts, display specific posts with their details, view comments on posts, and even publish new comments. It includes both the main script (`posts_proj.py`) and unit tests (`test_posts_proj.py`).

## Misc Information
1. My added function is a **profanity filter**
2. Data **validation** used throughout

## Files

- `posts_proj.py`: Contains the main functionality of the JSON Posts Project.
- `test_posts_proj.py`: Includes unit tests for the functions in `posts_proj.py`.

## Dependencies

- `requests`: Used for making HTTP requests to the JSONPlaceholder API.
- `profanity_check`: Utilised for detecting profanity in user comments.
- `random`: For randomising posts

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/kakaorigby/ecbobee_py
    ```

2. Navigate to the project directory:

    ```bash
    cd ecobee_py
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the main script:

    ```bash
    python posts_proj.py
    ```

5. Run unit tests:

    ```bash
    python test_posts_proj.py
    ```
