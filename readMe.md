## Features

- Generate text based on a user-provided prompt.
- Generate images based on the same prompt.
- Save generated text and images.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)


## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file at the root of the project to store your Hugging Face API token:

    ```bash
    touch .env
    ```

    In the `.env` file, add the following line:

    ```plaintext
    HUGGING_FACE_TOKEN=the_hugging_face_api_token
    ```

4. To run the project, execute:

    ```bash
    python main.py
    ```

## Examples of Prompts

Here are some example prompts you can use to test the generation:

- a beautiful girl
- a big wolf
- a butterfly effect cause