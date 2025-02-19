# Blog Project

A simple blog application built with Django, allowing users to create, read, update, and delete blog posts. Users can also register, log in, and manage their posts.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **CRUD Operations**: Users can create, read, update, and delete blog posts.
- **Post Management**: Each post is associated with a user (author).
- **Responsive Design**: The app is designed to be responsive and functional across devices.

## Prerequisites

Before running the application, ensure that you have the following installed:

- **Python** (preferably version 3.6 or above)
- **Django** (installed via pip)
- **SQLite** (used as the default database, no need to install separately)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/isakn2/blog_project.git
   cd blog_project
   ```

2. **Create a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies. Run the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   Install all the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can create one by running:

   ```bash
   pip freeze > requirements.txt
   ```

   You may need to install Django manually if it's not included in your `requirements.txt`:

   ```bash
   pip install django
   ```

4. **Apply migrations:**

   Run the following commands to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   If you want to access the Django admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create the superuser account.

6. **Run the development server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to view the blog.

   If you go to `http://127.0.0.1:8000/admin/`, you can log in with the superuser account to access the admin panel.

## Usage

1. **User Authentication**:
   - Register for a new account at `http://127.0.0.1:8000/accounts/register/`.
   - Log in at `http://127.0.0.1:8000/accounts/login/` to start managing posts.
   
2. **Managing Posts**:
   - View all blog posts at the home page (`http://127.0.0.1:8000/`).
   - Create a new post by navigating to `http://127.0.0.1:8000/post/new/`.
   - Edit or delete posts by visiting `http://127.0.0.1:8000/post/<post_id>/edit/` or `http://127.0.0.1:8000/post/<post_id>/delete/`.

3. **Admin Panel**:
   - Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage users and posts.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and create a pull request. Make sure to follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them
4. Push the changes to your fork (`git push origin feature-branch`)
5. Create a pull request

## License

This project is open-source and available under the MIT License.

---

### Customization Tips

- **Custom User Model**: If you want to use a custom user model, you can extend `AbstractUser` or `AbstractBaseUser`.
- **Deployment**: For deployment, consider using a more robust database like PostgreSQL instead of SQLite, and use a service like Heroku or DigitalOcean for hosting.

---

You can adjust the details as necessary (e.g., replace "yourusername" with your actual GitHub username). Let me know if you need more help with your `README.md` or any further customization!