# MedSecure System 🩺

A secure and scalable backend system for managing patients, doctors, and their relationships — built using **Django**, **Django REST Framework**, and **PostgreSQL** with **JWT Authentication**.

---

## 🚀 Features

- User registration and login (JWT-based)
- Patient record management (CRUD)
- Doctor record management (CRUD)
- Patient-doctor assignment mapping
- RESTful API endpoints
- Token-based authentication using `djangorestframework-simplejwt`
- PostgreSQL database integration
- Protected routes and input validation
- Modular structure using Django best practices

---

## 🛠️ Tech Stack

- **Python 3**
- **Django 5.2**
- **Django REST Framework**
- **PostgreSQL**
- **JWT Authentication** (`simplejwt`)
- **Decouple** for environment configuration

---

## 📂 Project Structure

```
MedSecure_System/
├── core/
│   ├── __init__.py
│   ├── admin.py             
│   ├── apps.py
│   ├── models.py               
│   ├── serializers/
│   │   ├── __init__.py
│   │   ├── auth_serializers.py
│   │   ├── doctor_serializers.py
│   │   ├── patient_serializers.py
│   │   └── mapping_serializers.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth_views.py
│   │   ├── doctor_views.py
│   │   ├── patient_views.py
│   │   └── mapping_views.py
│   ├── urls.py                  
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── [timestamp]_*.py     
│   └── tests.py                 
│
├── medsecure_backend/
│   ├── __init__.py
│   ├── settings.py              
│   ├── urls.py                  
│   ├── asgi.py
│   └── wsgi.py
│
├── .env
├── .gitignore 
├── manage.py
├── requirements.txt 
└── README.md             
```


---

## 🧪 API Endpoints

### 🔐 Authentication
| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/api/auth/register/`     | Register new user        |
| POST   | `/api/auth/login/`        | Obtain JWT access token  |
| POST   | `/api/auth/refresh/`      | Refresh JWT token        |

### 🧑‍⚕️ Doctor Management
| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/api/doctors/`           | Add new doctor           |
| GET    | `/api/doctors/`           | List all doctors         |
| GET    | `/api/doctors/<id>/`      | View doctor by ID        |
| PUT    | `/api/doctors/<id>/`      | Update doctor            |
| DELETE | `/api/doctors/<id>/`      | Delete doctor            |

### 🧑‍💼 Patient Management
| Method | Endpoint                  | Description                  |
|--------|---------------------------|------------------------------|
| POST   | `/api/patients/`          | Add new patient              |
| GET    | `/api/patients/`          | List your patients           |
| GET    | `/api/patients/<id>/`     | View patient by ID           |
| PUT    | `/api/patients/<id>/`     | Update patient               |
| DELETE | `/api/patients/<id>/`     | Delete patient               |

### 🔗 Patient-Doctor Mappings
| Method | Endpoint                          | Description                        |
|--------|-----------------------------------|------------------------------------|
| POST   | `/api/mappings/`                  | Assign doctor to patient           |
| GET    | `/api/mappings/`                  | List all mappings                  |
| GET    | `/api/mappings/<patient_id>/`     | Get mappings for a patient         |
| DELETE | `/api/mappings/delete/<id>/`      | Remove a specific mapping          |

---

🧰 Setup Instructions
1. Clone the repository
```
git clone https://github.com/Achal-Bharadwaj/medsecure-backend.git
cd medsecure-backend
```
2. Create a virtual environment
```
python -m venv env
env\Scripts\activate  # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Configure environment variables
Create .env file as shown above

5. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
6. Run the server
```
python manage.py runserver

```
🚀 Developed by Achal S Bharadwaj
🔗 GitHub: https://github.com/Achal-Bharadwaj\
