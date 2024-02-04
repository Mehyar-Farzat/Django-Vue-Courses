#Course Catalog App
This is a web application for browsing a course catalog. It consists of a REST API backend built with Django/DRF and a Vue.js frontend.

Backend
The Django backend provides a REST API for the course data.

Features
List courses
Filter courses by category
Retrieve course details
List categories
Usage
The API endpoints are:

/api/courses/ - List and filter courses
/api/courses/<id>/ - Retrieve a single course
/api/categories/ - List categories
Filtering
Courses can be filtered by category using the category query parameter. For example:

/api/courses/?category=1

Models
The main models are:

Category - Category model for organizing courses
Course - Course model containing details
Installation
Clone the repo
Create and activate a virtual env
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Load sample data: python manage.py loaddata courses/fixtures/courses.json
Run dev server: python manage.py runserver
Frontend
The Vue.js frontend is located in frontend/

It uses:

Vue 3
Vite
PrimeVue for UI components
Usage
To run the dev server:

cd frontend
npm install
npm run dev



The frontend will be available at http://localhost:5173/

It makes requests to the Django REST API backend.

License
This project is open source and available under the MIT License.
