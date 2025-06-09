# Social Website

A Django-based social website with user authentication, social login integration, and user profiles.

## Features

- User Authentication
  - Login/Logout functionality
  - Password change and reset
  - User registration
  - Custom user profiles
  - Email-based authentication

- Social Authentication
  - Google OAuth2 integration
  - Custom authentication backend
  - Social profile creation

- User Management
  - Extended user model
  - Profile management
  - Media file uploads
  - Secure password handling

## Technical Stack

- Python 3.x
- Django 5.2
- SQLite Database
- Social Auth (python-social-auth)
- Django Extensions

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/m7md158/SocialWebsite>
cd SocialWebsite
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following variables:
```
GOOGLE_OAUTH2_KEY=your_google_oauth2_key
GOOGLE_OAUTH2_SECRET=your_google_oauth2_secret
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

For HTTPS development server:
```bash
python manage.py runserver_plus --cert-file cert.crt
```

## Project Structure

- `account/` - User authentication and profile management
- `bookmarks/` - Main project configuration
- `media/` - User-uploaded files
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, images)

## Authentication Features

- Built-in Django authentication views:
  - PasswordChangeView
  - PasswordChangeDoneView
  - PasswordResetView
  - PasswordResetDoneView
  - PasswordResetConfirmView
  - PasswordResetCompleteView

## Security Features

- CSRF protection
- Secure password hashing
- Session management
- HTTPS support
- Secure file uploads

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

