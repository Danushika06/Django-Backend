# Student Management System — Django Backend

**A small Django REST backend with student and faculty records, written as a practice project that implements the same CRUD operations in several different Django and Django REST Framework styles.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/DRF-A30000?style=flat&logo=django&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

## Overview

This is a learning exercise rather than a finished product. The project (`college/`) has two apps, `students` and `faculty`, each exposing a handful of JSON endpoints over a SQLite database. There is no frontend and no authentication.

The interesting part is that the student endpoints deliberately show the same operations written several ways: plain Django function views with `JsonResponse` and `csrf_exempt`, DRF `APIView` classes with a serializer, and, in the faculty app, DRF generic views with mixins. It reads as a notebook of "how do I do this in Django" rather than a designed API.

Some of it is known to be unfinished or broken (listed under Usage), and I have left it that way rather than describe it as working.

## Key Features

- **Student CRUD in two styles** - the `Student` model (`name`, unique `email`, `department`, `cgpa`) is served both by function views in `students/views.py` and by DRF `APIView` classes (`Studentlist`, `StudentDetail`, `StudentCreate`, `StudentUpdate`, `StudentDelete`) using `StudentSerializer`.
- **Faculty CRUD with generic views** - `FacultyListCreate` combines `GenericAPIView` with `ListModelMixin` and `CreateModelMixin`; `FacultyUpdate` extends `RetrieveUpdateDestroyAPIView`.
- **Small URL and request experiments** - path parameters with `<int:idd>/<str:name>/`, a query-string handler (`home`) and a `debug_view` that prints the request method, path and headers to the console.
- **Django admin** - both models are registered in their apps' `admin.py`.

## How It Works

`college/college/urls.py` mounts `admin/`, `students/` and `faculty/`. Each app has its own `urls.py`, models, migrations (`0001_initial`) and, where used, a serializer module. The project uses the default SQLite database (`db.sqlite3`) and `rest_framework` is listed in `INSTALLED_APPS` in `college/college/settings.py`.

For the DRF views, request data goes through `StudentSerializer` or `FacultySerializer` (both `ModelSerializer` with `fields = "__all__"`), which validates and saves. The plain Django views parse `request.body` with `json.loads` and build `JsonResponse` objects by hand.

## Tech Stack

- **Language:** Python
- **Framework:** Django (the settings file says it was generated with Django 6.1) and Django REST Framework
- **Database:** SQLite
- **Dependencies:** no `requirements.txt` in the repo, so versions are not pinned

## Getting Started

### Prerequisites
- Python 3 with `pip`

### Installation
```bash
git clone https://github.com/Danushika06/Django-Backend.git
cd Django-Backend/college
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install django djangorestframework
```
There is no requirements file, so the two packages above are what the code imports. Pick a Django version that matches your Python.

### Running
```bash
python manage.py migrate
python manage.py runserver
```
The server starts on `http://127.0.0.1:8000/`.

## Usage

Student endpoints (prefix `/students/`):

| Method | Path | Style | Behaviour |
|--------|------|-------|-----------|
| GET | `list/` | DRF `APIView` | List all students |
| GET | `students/` | function view | List all students as JSON |
| GET | `detail/<id>/` | DRF `APIView` | One student |
| GET | `<id>/` | function view | One student, 404 JSON if missing |
| POST | `createe/` | DRF `APIView` | Create via serializer |
| POST | `create/` | function view | Create from a JSON body (see note) |
| PUT | `updatee/<id>/` | DRF `APIView` | Update via serializer |
| PUT | `update/` | function view | Update, student `id` in the JSON body |
| DELETE | `deleteee/<id>/` | DRF `APIView` | Delete by id |
| DELETE | `delete/` | function view | Delete, student `id` in the JSON body |
| GET | `<id>/<name>/`, `debug/`, `home/?department=` | function views | Path/query/debug experiments |

Faculty endpoints (prefix `/faculty/`):

| Method | Path | Behaviour |
|--------|------|-----------|
| GET, POST | `list` | List or create faculty (`name`, `email`, `phone`) |
| GET, PUT, PATCH, DELETE | `update/<id>/` | Retrieve, update or delete one faculty record |
| any | `` | Echoes the HTTP method |

Known problems I can see in the code:
- `create_students` indexes `body.get["name"]` instead of calling `body.get("name")`, so the function-view create endpoint fails with an error.
- `update_students` calls `json.loads` before checking the method and returns nothing for non-PUT requests.
- The DRF `StudentDetail` and `StudentUpdate` views use `Student.objects.get` without handling a missing row.
- No authentication or permissions on any endpoint, and the function views are `csrf_exempt`.
- Settings are the development defaults (`DEBUG = True`, `ALLOWED_HOSTS = ['*']`, the generated insecure secret key) and include a `MAILERS` block that is not a Django setting.
- There are no real tests; both `tests.py` files are the empty stubs.

## Project Structure

```
Django-Backend/
└── college/
    ├── manage.py
    ├── college/            # project: settings.py, urls.py, wsgi/asgi
    ├── students/           # Student model, serializer, function + APIView endpoints
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   ├── views.py
    │   └── migrations/
    ├── faculty/            # Faculty model, serializer, generic DRF views
    │   ├── models.py
    │   ├── serializer.py
    │   ├── urls.py
    │   ├── views.py
    │   └── migrations/
    └── db.sqlite3          # committed development database
```

---

## Contact

<table>
  <tr><td><b>GitHub:</b> <a href="https://github.com/Danushika06">Danushika06</a></td><td><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/danushika-n-323b4628b/">danushika-n</a></td></tr>
  <tr><td colspan="2" align="center"><b>Email:</b> <a href="mailto:danushikanagarajan@gmail.com">danushikanagarajan@gmail.com</a></td></tr>
</table>

Built by **Danushika N**
