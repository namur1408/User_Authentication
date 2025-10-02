# FastAPI User Authentication Project

A simple educational project built with FastAPI implementing user registration, login, and logout, with SQLAlchemy for database management. Users can also upload an avatar to their profile.


## Features

- User registration with password hashing (bcrypt)
- User login with password verification
- User logout (clearing cookie)
- Profile page with avatar upload
- Jinja2 templates for rendering pages
- Simple authentication via cookie (`user_id`)


## Installation

1. Clone the repository:

```bash
    git clone https://github.com/namur1408/User_Authentication.git
    cd User_Authentication
```
2. Install dependencies:
```bash
  pip install -r requirements.txt
```
3. Create file static and file avatars in it
   
4. Run the application:
```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
``` 
5. Open your browser and go to the link that was given to you

   
##  Project Structure
```text
recipes-app/
│
├── static/                # Static files (CSS, images, avatars)
│   ├── avatars/
│         ├── # Your photo will be created here
├── templates/             # Jinja2 templates
│   ├── base.html          
│   ├── login.html          
│   ├── profile.html         
│   └── register.html         
├── auth.py                # Routes for authentication
├── database.py            # Database setup (SQLAlchemy)
├── main.py                # App entry point
├── models.py              # SQLAlchemy models
├── profile.py             # Profile and avatar routes
├── requirements.txt       # Python dependencies
├── schemas.py             # Pydantic schemas
└── templates.py           # Template setup
```


## Technologies Used

- Python 3.13

- FastAPI

- SQLAlchemy

- Jinja2

- bcrypt & passlib

- Uvicorn


## Notes

- This is an educational project.

- Authentication via cookies is not secure for real-world apps.

- Passwords are hashed using bcrypt.

- The project can be extended with JWT authentication, email verification, and session management.
