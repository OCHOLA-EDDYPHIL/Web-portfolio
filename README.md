# Portfolio Project
This is a **Django-based portfolio web application**. The project integrates various tools and frameworks like **Bootstrap 5** and **SweetAlert** to reinforce a robust and modern user interface while leveraging Django’s backend strengths.
## Features
### 1. **Django Framework**
- Built on the **Django 4.1.7** framework, which provides a flexible and extensible foundation for web applications.

### 2. **Portfolio Application**
- Contains the `portfolioapp`, which handles the main functionality, including showcasing skills, projects, and services.

### 3. **Bootstrap Integration**
- **Bootstrap 5** is used to simplify responsive and consistent front-end design.
- Ensures cross-device compatibility and user-friendly interfaces.

### 4. **SweetAlert Integration**
- Uses **SweetAlert** to replace default JavaScript alerts with dynamic and visually enhanced pop-ups.
- Displays user-friendly feedback for various actions, including success, error, confirmation, and information messages.
- Example use cases in the project:
    - **Welcome Message**: Users visiting the homepage are greeted with a custom informational alert.
    - **Submission Feedback**:
        - Success alerts for form submissions (e.g., reviews, project uploads, or applications).
        - Error alerts for invalid inputs or failed processes.

    - **Interactive Messaging**: Alerts tied to specific actions (e.g., submitting a review or updating projects).

- Configured to work seamlessly with Django’s message framework, making it easy to trigger alerts from views.

### 5. **Template System**
- Leveraging Django’s template engine for structured and efficient rendering.
- Custom template directory (`templates`) ensures reusability and modularity while maintaining flexibility for different pages, components, and user interactions.

### 6. **Static and Media File Management**
- Configured to manage CSS, JavaScript, and images under `static/`.

### 7. **Dynamic Content**
- Enables the display of dynamic content like services, reviews, and projects using Django's ORM and context data from views.

### 8. **User Authentication**
- Django’s default authentication system secures access to admin features like managing applications and projects.
- Role-based access ensures only authorized users can add and view private content.

### 9. **Contact Form and Submissions**
- A contact form allows users to submit their applications, projects, and reviews with active validation and feedback via SweetAlert.

### 10. **Database**
- Powered by SQLite3 with prebuilt models for services, projects, reviews, and user applications.

### 11. **Seamless Notifications**
- Using Django's message framework in combination with SweetAlert for user notifications. Alerts auto-close after a fixed time or remain until user acknowledges them.

### 12. **Internationalization**
- Configured for English (US) with timezone support (`UTC`).

## SweetAlert in Action
SweetAlert adds a polished, professional touch to the app’s user experience. It is used in scenarios like the following:
1. **Welcome Alert:**
    - Purpose: Display a friendly introduction upon visiting the homepage.
    - Example:
``` text
     Welcome to my portfolio! I’m Leroy Eugene Oroni.
```
1. **Form Success/Error Feedback:**
    - Example (Success):
``` text
     Your application was submitted successfully. We’ll get back to you shortly!
```
- Example (Error):
``` text
     Sorry, there was a problem with your submission. Please try again.
```
1. **Review Submission Feedback:**
    - Alerts users whether their review has been submitted successfully or failed validation.

2. **Dynamic Messaging:**
    - Django's `messages` framework works with SweetAlert to provide real-time feedback for any server-side actions.

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
## SweetAlert Setup Guide
1. SweetAlert is imported in `index.html` via the following CDN:
``` html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js"></script>
```
This ensures that SweetAlert is globally available for interactive and visually appealing alerts.
1. Messages Framework Integration:
    - SweetAlert is dynamically triggered in the template using Django’s `messages` framework. For example:
``` djangotemplate
     {% if messages %}
       <script>
           {% for message in messages %}
               swal({
                   text: "{{ message }}",
                   icon: "{{ message.tags }}",
                   timer: 20000,
               });
           {% endfor %}
       </script>
     {% endif %}
```
This approach enables seamless connection between backend message handling and front-end alerts.
## Future Enhancements
- Expand SweetAlert functionality for form validations directly on the client side.
- Allow for multi-step SweetAlert forms for better user experience.
- Add SweetAlert themes to further align with branding.

## Folder Structure
``` text
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
├── templates/         # HTML templates for different views
│   └── ...
│
├── static/            # Static files directory
│   └── ...
│
├── db.sqlite3         # SQLite database file
└── manage.py          # Django management script
```
## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
This README now fully incorporates **SweetAlert** as a key feature while ensuring clarity and completeness. Let me know if further refinements are needed! 🎉
