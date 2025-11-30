------------------------------------------------
Helpdesk Ticket System 🎫
------------------------------------------------

A modern Django-based helpdesk ticket management system with full user authentication and staff management capabilities.

https://img.shields.io/badge/Django-5.2.8-green
https://img.shields.io/badge/Python-3.13-blue
https://img.shields.io/badge/Database-SQLite-lightgrey

✨ Features
🔐 User Authentication - Secure registration and login system

🎫 Ticket Management - Create, update, and track support tickets

👥 Role-Based Access - Separate interfaces for users and staff

📊 Staff Dashboard - Comprehensive ticket queue management

🎨 Responsive Design - Works on desktop and mobile devices

🔧 Admin Panel - Full Django admin interface

🚀 Quick Start
Prerequisites
Python 3.8+

pip package manager

Installation
Clone the repository

bash
git clone https://github.com/yourusername/helpdesk-project.git
cd helpdesk-project
Set up virtual environment

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run migrations

bash
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Start development server

bash
python manage.py runserver
Access the application

Main site: http://localhost:8000

Admin panel: http://localhost:8000/admin

📁 Project Structure
text
helpdesk_project/
├── accounts/                 # User authentication app
│   ├── models.py            # Custom user models
│   ├── views.py             # Authentication views
│   ├── urls.py              # Auth routes
│   └── templates/accounts/   # Auth templates
├── tickets/                  # Ticket management app
│   ├── models.py            # Ticket models
│   ├── views.py             # Ticket views
│   ├── urls.py              # Ticket routes
│   └── templates/tickets/   # Ticket templates
├── templates/               # Base templates
│   ├── base.html            # Main layout
│   └── registration/        # Django auth templates
├── static/                  # Static files
│   ├── css/
│   └── js/
├── manage.py
└── requirements.txt
👥 User Roles
🔧 Staff Users
Access to staff dashboard

View all tickets in the system

Assign tickets to themselves

Update ticket status and priority

Close resolved tickets

👤 Regular Users
Create new support tickets

View their own tickets

Update their own open tickets

Track ticket status and updates

🎯 Usage
For End Users
Register a new account at /accounts/register/

Login to your account at /accounts/login/

Create tickets for technical issues or support requests

Track progress of your submitted tickets

Update tickets with additional information if needed

For Staff
Access dashboard at /tickets/dashboard/

View ticket queue with filtering options

Assign tickets to yourself or team members

Update status as you work on tickets

Close tickets when issues are resolved

⚙️ Configuration
Environment Settings
Update settings.py for production:

python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-secure-secret-key'
Database
Default SQLite configuration (update for production):

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
🛠️ Customization
Adding New Ticket Fields
Edit tickets/models.py:

python
class Ticket(models.Model):
    # Add new fields here
    custom_field = models.CharField(max_length=100)
Modifying Templates
All templates are located in the templates/ directory and can be customized to match your organization's branding.

🤝 Contributing
Fork the project

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🐛 Bug Reports
If you encounter any bugs or have suggestions, please open an issue on GitHub.

🙏 Acknowledgments
Django framework and community

Bootstrap for frontend components

Contributors and testers
