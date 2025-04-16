<<<<<<< HEAD
# Django User Profile System

A modern and feature-rich user profile system built with Django. This system allows users to create profiles, manage their information, and showcase their professional details.

## Features

- 🔐 User Authentication
  - Registration
  - Login/Logout
  - Password Management
  - Last Login Tracking

- 👤 Profile Management
  - Profile Picture Upload
  - Basic Information (Bio, Location, Birth Date)
  - Contact Information (Phone, Email)
  - Social Media Links (Facebook, Twitter, LinkedIn)
  - Professional Information (Skills, Education, Work Experience)

- 🎨 Modern UI/UX
  - Responsive Design
  - Bootstrap 5 Styling
  - Custom CSS Animations
  - Font Awesome Icons
  - Profile Completion Progress Bar

- 📊 Profile Statistics
  - Profile Views Counter
  - Last Active Time
  - Profile Completion Percentage
  - Visual Progress Indicators

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd profile
```

2. Create and activate virtual environment:
```bash
python -m venv env
# On Windows
env\Scripts\activate
# On Unix or MacOS
source env/bin/activate
```

3. Install required packages:
```bash
pip install django pillow
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. **Registration**
   - Visit: http://127.0.0.1:8000/register/
   - Fill in your details
   - Create your account

2. **Login**
   - Visit: http://127.0.0.1:8000/accounts/login/
   - Enter your credentials
   - Access your profile

3. **Profile Management**
   - View Profile: http://127.0.0.1:8000/profile/
   - Edit Profile: http://127.0.0.1:8000/profile/edit/
   - Update your information
   - Upload profile picture
   - Add social media links

## Project Structure

```
profile/
├── manage.py
├── userprofile/          # Main project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── profiles/            # Main app directory
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── profiles/
│       └── registration/
├── static/             # Static files
│   ├── css/
│   ├── js/
│   └── img/
├── media/              # User uploaded files
│   └── avatars/
└── templates/          # Project templates
    ├── base.html
    ├── profiles/
    └── registration/
```

## Customization

1. **Email Configuration**
   - Update email settings in `settings.py`
   - Configure your email backend
   - Set up SMTP settings

2. **Profile Fields**
   - Modify `profiles/models.py` to add/remove fields
   - Update forms in `profiles/forms.py`
   - Adjust templates in `templates/profiles/`

3. **Styling**
   - Edit `static/css/style.css`
   - Modify Bootstrap classes in templates
   - Add custom JavaScript in `static/js/`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers.

## Acknowledgments

- Django Framework
- Bootstrap 5
- Font Awesome Icons
- All contributors and users 
=======
# Profile
>>>>>>> 3725ef90bd2d394463f3a675bf18022420b2a5f0
