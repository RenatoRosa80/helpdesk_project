Helpdesk Django Project - Completed Minimal Version
--------------------------------------------------
This is a ready-to-run Django project (minimal, educational) implementing a Help Desk system.

Quickstart (recommended inside a virtualenv):

1. python -m venv venv
2. source venv/bin/activate   # Windows: venv\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Admin: /admin/
Tickets: /tickets/
Accounts: /accounts/

Notes:
- This project uses SQLite (db.sqlite3)
- Groups 'Clientes' and 'StaffTI' can be created via admin or shell.


ADMIN USER CREATION: Registro público foi removido. Crie usuários via /accounts/admin/users/ (apenas superuser) ou via Django admin.
