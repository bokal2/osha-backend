# Cleaning Services Management API

This is a Django-based project for managing cleaning services. It uses the Django Rest Framework (DRF) to provide RESTful APIs, JWT for authentication and authorization, and PostgreSQL as the database backend.

## Features

- **Service Management**: Create, update, and delete cleaning services.
- **Client Management**: Manage client information.
- **Booking System**: Allow clients to book cleaning services.
- **Authentication and Authorization**: Secure endpoints using JWT.
- **Data Persistence**: Utilize PostgreSQL for reliable data storage.

---

## Technologies Used

- **Backend Framework**: Django, Django Rest Framework
- **Authentication**: JSON Web Tokens (JWT) via `djangorestframework-simplejwt`
- **Database**: PostgreSQL
- **Environment Management**: `python-dotenv` for environment variables
- **Deployment Ready**: Configurable for cloud deployment (e.g., AWS, Heroku)

---

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/bokal2/osha-backend.git
   cd osha-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root and add the following:
     ```env
     SECRET_KEY=your_secret_key_here
     DEBUG=True
     DATABASE_NAME=cleaning_services_db
     DATABASE_USER=your_db_user
     DATABASE_PASSWORD=your_db_password
     DATABASE_HOST=localhost
     DATABASE_PORT=5432
     ```

5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

Access the application at `http://127.0.0.1:8000/`.

---

## Testing

Run the tests using:
```bash
python manage.py test
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)
