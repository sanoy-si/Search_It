# Search_it Simple Search Engine

This project is a simple search engine that ranks documents using a vector space model and cosine similarity. The web application is built with Django for the backend and HTML, CSS, Bootstrap, and JavaScript for the frontend.

## Features

- Indexes and searches documents
- Ranks documents using vector space model and cosine similarity
- Web-based interface for querying and displaying results

## Technologies Used

### Backend

- Django (Python)
- Numpy
- Scikit-learn
- NLTK
- PyPDF2
- Python-docx

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

## Prerequisites

- Python

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/saleamlakw/Search_it.git
    cd Search_it
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```


4. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

## Running the Development Server

Start the Django development server:

```bash
python manage.py runserver

```
## Visit http://127.0.0.1:8000/ in your web browser to see the application in action.
homepage
<img width="952" alt="search" src="https://github.com/user-attachments/assets/036b830c-05c8-4505-bbea-f4937698c9a8">
resultpage
<img width="959" alt="result" src="https://github.com/user-attachments/assets/3297d47e-6962-441e-bfc1-d1fc5502022a">
