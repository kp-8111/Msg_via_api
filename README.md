# msg_project

A Django-based web application that fetches a random quote from an external API and displays it on the homepage.

## Features

- **Homepage**: Displays a random quote when the button is clicked.
- **Admin Panel**: Standard Django admin interface for managing the project.
- **API Integration**: Fetches random quotes from the ZenQuotes API.

## Technologies Used

- **Django**: Web framework for building the app.
- **Python**: Programming language used.
- **Requests**: Python library for making HTTP requests to fetch data from the ZenQuotes API.
- **SQLite**: Default database used for development.

## Installation

### Prerequisites

- Python 3.x
- Django 4.2.x

### Steps to Set Up Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/msg_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd msg_project
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- Visit the homepage to see a random quote fetched from the ZenQuotes API.
- Click the button on the homepage to refresh the quote.
- The project also includes the default Django admin panel, accessible at `http://127.0.0.1:8000/admin/` for administrative tasks.



