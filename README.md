!##Django-Vue-Courses
Django-Vue-Courses is a web application that allows users to browse and enroll in courses. It consists of a backend Django/DRF API and a frontend built with Vue.js.

Features
Browse courses by category
View course details including name, description, instructor, reviews, and more
Enroll in courses
Manage user account
Admin portal to manage courses, categories, instructors, etc
Backend
The backend is a REST API built with:

Django
Django REST Framework
Django Filter
JWT Authentication
It includes endpoints for:

Courses
Categories
Enrollments
Users and authentication
Instructors
Reviews
The admin site allows managing all models and data.

Frontend
The frontend allows users to:

Browse courses
View course details
Enroll in courses
Manage account
And more...
It is built with:

Vue 3
Vue Router
Vuex (state management)
Axios (API requests)
Tailwind CSS
Installation
Backend
# Clone repo
cd backend

# Virtualenv
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Load data
python manage.py loaddata courses/fixtures/*.json

# Run development server
python manage.py runserver



Frontend
# Change into frontend directory 
cd frontend

# Install dependencies
npm install

# Run dev server
npm run dev



Contributing
Contributions are welcome! Please open an issue or PR.

License
This project is open source and available under the MIT License.

