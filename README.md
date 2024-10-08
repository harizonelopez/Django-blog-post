# Django-blog post Project.

This is a simple Django project for creating, editing, and deleting blog posts.

## Features

- Create new blog posts
- Edit existing blog posts
- Delete blog posts
- Flash messages for actions (create, edit, delete)
- User-friendly interface with Bootstrap

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/harizonelopez/Django-blog-post.git
    cd Django-blog-post
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv
    source venv/Scripts/activate   # On Mac venv/bin/activate
    ```

3. **Set up the database:**

    ```sh
    python manage.py migrate
    python manage.py makemigrations
    ```

4. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

5. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000
    ```

## Usage

### Creating a New Post

1. Click on the "new post" link on the homepage.
2. Fill in the form and submit to create a new post.

### Editing a Post

1. On the homepage, click the "Edit" icon below the post you want to edit.
2. Update the post information and submit the form to save the changes.

### Deleting a Post

1. On the homepage, click the "Trash" icon below the post you want to delete.
2. Confirm the deletion in the pop-up window.

### Flash Messages

- Success messages are displayed for creating, editing, and deleting the posts.
- The flashed messages disappear after a few seconds.

## Contributing

1. **Fork the repository**
2. **Create a new branch**

    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m 'add new feature'
    ```    
