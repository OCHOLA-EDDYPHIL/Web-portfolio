# Portfolio Project

This is a **Django-based portfolio web application**. The project leverages Django's features to create a lightweight
and easily extendable personal portfolio. The app integrates various tools and frameworks to ensure a robust and modern
web interface.

## Features

### 1. **Django Framework**

- Built on the **Django 4.1.7** framework, which provides a well-structured and extensible foundation for creating web
  applications.

### 2. **Portfolio Application**

- The `portfolioapp` app is the core feature of this project. It handles the main functionality, likely including
  portfolio elements such as skills, projects, or experiences.

### 3. **Bootstrap Integration**

- Integrated **Bootstrap 5** for front-end responsiveness and UI consistency.
- The `bootstrap5` package is added to enhance the design and styling of the application.

### 4. **Template System**

- Utilizes the Django **template engine** with a centralized structure:
    - Templates stored in a dedicated `templates` directory within the project.

- Context processors are configured to ensure global access to needed variables across templates.

### 5. **User Authentication**

- Uses Django's default authentication system for user login/logout and permissions management.
- Authentication middleware integrates securely with sessions.

### 6. **Static Files Management**

- Static files (CSS, JavaScript, Images) are centrally managed through the `STATIC_URL` setting.
- Configured static files directory: `static/`.

### 7. **Database**

- Uses SQLite3 as the database, providing a lightweight and easy-to-setup solution for development.
- Includes predefined configurations for database migrations and schema management.

### 8. **Middleware**

- Includes essential middleware for security, sessions, CSRF protection, and more.

### 9. **Secure Password Validation**

- Implements Django’s default password validation features:
    - Checks for common password vulnerabilities.
    - Ensures a minimum length and other customizable constraints.

### 10. **Internationalization**

- Configured for English (United States) as the default language (`LANGUAGE_CODE='en-us'`) and the UTC timezone.

### 11. **Project Modularity**

- The modular project structure ensures clean separation between apps, configurations, and templates. Core components
  include:
    - `portfolio` (main Django project configuration files).
    - `portfolioapp` (custom app for portfolio-specific functionality).

## Setup and Installation

### Requirements:

- Python 3.12.8
- Django 4.1.7

### Steps:

1. **Clone the Repository**:

``` bash
   git clone <repository-url>
   cd portfolio
```

1. **Create a Virtual Environment**:

``` bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
```

1. **Install Dependencies**:

``` bash
   pip install -r requirements.txt
```

1. **Database Migrations**:

``` bash
   python manage.py migrate
```

1. **Run the Development Server**:

``` bash
   python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000`.

## Folder Structure

``` 
portfolio/
│
├── portfolio/         # Main Django project folder
│   ├── settings.py    # Project settings
│   ├── urls.py        # Project-level URL configuration
│   ├── wsgi.py        # WSGI entry point
│   └── ...
│
├── portfolioapp/      # Portfolio application folder
│   ├── migrations/    # Database migrations
│   ├── models.py      # Database models
│   ├── views.py       # Application views
│   ├── urls.py        # Application-level URLs
│   └── ...
│
├── templates/         # Custom templates directory
│   └── ...
│
├── static/            # Static files directory
│   └── ...
│
└── db.sqlite3         # SQLite database file
```

## Future Enhancements

- Add more features such as admin panel customization.
- Implement deployment settings for production, including:
    - Secure `SECRET_KEY` management.
    - Hosting and scaling solutions (e.g., using Heroku or AWS).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
Feel free to reach out in case of questions or implementation issues! 🎉
