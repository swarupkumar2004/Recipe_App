# Recipe_App
---
# 🍲 Recipe App

A simple recipe management app built using Django with REST API support, PostgreSQL database, and Django templates for frontend. Users can add, edit, delete, and view recipes with login authentication.

---

## 🔧 Tech Stack

- **Backend**: Python, Django 5.2.3, Django REST Framework
- **Frontend**: Django Templates (HTML only)
- **Database**: PostgreSQL
- **Realtime Ready**: Django Channels + Redis (optional setup included)

---

## 🚀 Features

- User authentication (Login/Logout)
- Add new recipes with category, ingredients, and instructions
- View all recipes
- Edit and delete your own recipes
- Admin panel for superuser
- REST API for recipes (`/api/recipes/`)

---

## 🗂 Project Structure

```

Recipe\_App/
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py / wsgi.py
├── recipes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── add\_recipe.html
│   │   ├── edit\_recipe.html
│   │   ├── delete\_recipe.html
│   │   └── registration/
│   │       └── login.html
├── static/ (optional)
├── templates/ (global templates directory)
├── manage.py

````

---

## 🛠️ Setup Instructions

### 1. Clone and navigate

```bash
git clone <your-repo-url>
cd Recipe_App
````

### 2. Create Virtual Environment

```bash
python -m venv myvenv
myvenv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL in `backend/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recipe_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Migrate and Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔒 Login Credentials

* Access `/admin/` for admin dashboard
* Or use the Login button on the homepage

---

## 📬 API Endpoint

* `/api/recipes/` - Full CRUD using Django REST Framework

---

## 📦 Static Files

If you use static files:

```bash
python manage.py collectstatic
```

---

## ✅ Status

✔️ Fully working CRUD Recipe App
✔️ Supports both HTML templates and REST API
✔️ Authenticated views for edit/delete

---

## 📄 License

This project is licensed under the MIT License.

```

---

Let me know if you want this zipped or converted into a downloadable `.md` file.
```
