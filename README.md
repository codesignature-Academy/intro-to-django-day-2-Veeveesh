[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Q15cif73)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24194368&assignment_repo_type=AssignmentRepo)
# Day 2 Assignment — Django Apps & URL Routing

## What You're Building

Starting from your Day 1 `todo_project`, you'll create a `tasks` app and wire up three routes: **Home**, **About**, and **Contact** — each with its own view and a named URL.

This is the foundation the rest of the to-do app will be built on top of in later days.

---

## Requirements

### 1. Create and register the `tasks` app
- Run `python manage.py startapp tasks` inside your project.
- Add `'tasks'` to `INSTALLED_APPS` in `settings.py`.

### 2. Build three views
In `tasks/views.py`, write three function-based views:
- `home` — returns a response for the homepage.
- `about` — returns a response describing the app.
- `contact` — returns a response with some way to get in touch (a placeholder is fine).

You can use `HttpResponse` directly for now — templates aren't required until Day 4.

### 3. Wire up named URL routes
In `tasks/urls.py`, create three `path()` entries, each with a `name`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

### 4. Connect `tasks/urls.py` to the project
In your project's main `urls.py` (next to `settings.py`), include the tasks app's URLs:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```

### 5. Confirm it all runs
- `python manage.py runserver`
- Visit `/`, `/about/`, and `/contact/` and confirm each loads without errors.

---

## Submission Checklist

- [ ] `tasks` app created via `startapp` and registered in `INSTALLED_APPS`
- [ ] `home`, `about`, and `contact` views exist in `tasks/views.py`
- [ ] `tasks/urls.py` defines all three routes with `name=` set
- [ ] Project's root `urls.py` includes `tasks.urls`
- [ ] Server runs with no errors; all three routes return a working page
- [ ] Commit history shows your progress (not one giant commit)
- [ ] README updated with a short note on what `name=` does for a URL and why it's useful

## Homework Questions (answer in your README)

1. In your own words, explain the difference between a project and an app.
2. What command creates a new Django app?
3. Why do we register an app inside `INSTALLED_APPS`?
4. What does giving a URL a `name=` actually let you do later?

---

## Autograding

This repo includes automated checks (`.github/workflows/classroom.yml`) that verify:
- the `tasks` app exists and is registered
- `python manage.py check` passes
- all three named routes resolve and return a successful response
- no virtual environment was committed

These checks cover the mechanical parts of the assignment. Your README explanations and homework answers are graded separately by your instructor.

## My readme answer " what 'name=' does for a URL and why it's useful"
'name = ' allows you to assign a name to a URL so that it can always be assessed even without the file path by referencing the name .
It is useful because without it , a change in the filepath will cause the URL to be inaccessible

## My Homework answers
1. explain the difference between a project and an app. : 
 A project is the whole site you will be working on(picture it as a School) while an app is only a feature that does a thing in the project( picture this as classrooms in the school, each class might be handling a different subject or level)
2. What command creates a new Django app?
 The command is  
            python manage.py startapp 'the_app_name'
3. Why do we register an app inside 'INSTALLED_APPS'?
 the settings.py contains the configurations of the project that we are working on and allows the app to fuction in the project, without it the default home page may not be overriden as it may not even be assessed
4.  What does giving a URL a 'name=' actually let you do later?
it allows you to navigate to the exact url that you want to assess, by matching it to the name that you have assigned it 