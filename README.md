msg_project
A Django-based web application that fetches a random quote from an external API and displays it on the homepage.

Features
Homepage: Displays a random quote when the button is clicked.
Admin Panel: Standard Django admin interface for managing the project.
API Integration: Fetches random quotes from the ZenQuotes API.
Technologies Used
Django: Web framework for building the app.
Python: Programming language used.
Requests: Python library for making HTTP requests to fetch data from the ZenQuotes API.
SQLite: Default database used for development.
Installation
Prerequisites
Python 3.x installed.
Django 4.2.x installed.
Steps to Set Up Locally
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/msg_project.git
Navigate to the project directory:

bash
Copy code
cd msg_project
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the dependencies: Make sure you have a requirements.txt file in the root directory. If not, you can create one manually.

bash
Copy code
pip install -r requirements.txt
Run the migrations to set up the database:

bash
Copy code
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver
Access the application: Open your browser and go to http://127.0.0.1:8000/ to see the homepage with a random quote.

Usage
Visit the homepage to see a random quote fetched from the ZenQuotes API.
Click the button on the homepage to refresh the quote.
The project also includes the default Django admin panel, accessible at http://127.0.0.1:8000/admin/ for administrative tasks.
Project Structure
msg_project/: Main project folder containing settings, URLs, and WSGI configurations.
mpapp/: The Django app that contains the core functionality and views for the homepage.
templates/: Folder containing HTML templates, including home.html.
License
MIT License - see LICENSE for details.

