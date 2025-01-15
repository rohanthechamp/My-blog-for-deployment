# Flask Blog Project

This project is a Flask-based blogging platform that allows users to register, log in, create, edit, and delete blog posts. Users can also comment on blog posts, and the platform features an admin-only functionality for managing posts and comments.

---

## Features

### User Authentication
- **Register**: Users can register with a name, email, and password. Passwords are hashed using `Werkzeug` for secure storage.
- **Login**: Registered users can log in using their email and password.
- **Logout**: Users can log out of their accounts.

### Blog Post Management
- **Create Posts**: Admin users can create new blog posts.
- **Edit Posts**: Admin users can edit existing blog posts.
- **Delete Posts**: Admin users can delete blog posts.
- **View Posts**: All users can view blog posts.

### Comment System
- **Post Comments**: Logged-in users can leave comments on blog posts.
- **Delete Comments**: Admin users can delete any comment.

### Admin Functionality
- Only users with an `id` of `1` (default admin user) have access to create, edit, or delete posts and comments.

### Additional Features
- **Gravatar Integration**: User avatars are displayed using `Flask-Gravatar`.
- **Rich Text Editor**: Blog content and comments support rich text formatting using `Flask-CKEditor`.
- **Form Validation**: User inputs are validated using `WTForms`.
- **Sanitization**: Blog content is sanitized using `bleach` to prevent XSS attacks.

---

## Technologies Used

### Backend
- **Flask**: Web framework.
- **Flask-WTF**: Form handling and validation.
- **Flask-CKEditor**: Rich text editor for blog content and comments.
- **Flask-SQLAlchemy**: ORM for database management.
- **Flask-Login**: User authentication and session management.
- **Flask-Bootstrap**: UI styling with Bootstrap 5.

### Database
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database for development and testing (can be configured for other DBs).

### Security
- **Werkzeug**: For password hashing.
- **Bleach**: For sanitizing user inputs.

### Deployment
- **Python-dotenv**: For managing environment variables.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-blog
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt  (replace the versions with latest one at that time )
   ```
5. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     Flask_Secret_Key=your_secret_key
     DATABASE_URL=sqlite:///blog.db
     ```
6. Initialize the database:
   ```bash
   flask shell
   from app import db
   db.create_all()
   exit()
   ```
7. Run the application:
   ```bash
   flask run
   ```
8. Access the application at `http://127.0.0.1:5000/`.

---

## Usage

### Access Levels
- **Admin**: Full control over blog posts and comments.
- **Regular Users**: Can view posts and add comments.
- **Guest Users**: Can view posts but cannot comment or create posts.

### Endpoints
- `/`: Home page displaying all blog posts.
- `/register`: Register a new user.
- `/login`: Log in an existing user.
- `/logout`: Log out of the account.
- `/new-post`: Create a new blog post (admin-only).
- `/edit-post/<post_id>`: Edit an existing blog post (admin-only).
- `/delete/<post_id>`: Delete a blog post (admin-only).
- `/post/<post_id>`: View a single blog post and its comments.
- `/delete_comment/<comment_id>`: Delete a comment (admin-only).
- `/about`: About page.
- `/contact`: Contact page.

---

## Project Structure

```
flask-blog/
├── static/         # Static files (CSS, JS, images)
├── templates/      # HTML templates
├── app.py          # Main Flask application
├── forms.py        # WTForms classes
├── models.py       # SQLAlchemy models
├── requirements.txt# Python dependencies
├── .env            # Environment variables
└── README.md       # Project documentation
```

---

## Future Improvements

- Add support for user profile pages.
- Implement email verification during registration.
- Add pagination for blog posts and comments.
- Enhance admin panel with analytics.
- Allow users to reset passwords via email.



