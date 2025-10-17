# odyseeyHackathonps1

A Django-based hackathon project for rapid prototyping with modular apps, basic authentication, media handling, and a simple project layout suitable for extension.

## Features
- Modular Django apps (authentication, home, etc.)
- Basic authentication (signup/login, sessions)
- Media file handling (CSV and other uploads)
- Organized static files and templates
- Multi-language codebase: Python (Django), Cython/C/C++, CSS/SCSS
- Simple workflow for contributors

## Requirements
- Python 3.8+
- pip
- (Optional) virtualenv or venv
- See `requirements.txt` for Python packages

## Quickstart / Setup
1. Clone the repository
    ```
    git clone https://github.com/Kaditya67/odyseeyHackathonps1.git
    cd odyseeyHackathonps1
    ```
2. Create and activate virtual environment (recommended)
    - Windows:
      ```
      python -m venv .venv
      .venv\Scripts\activate
      ```
    - macOS / Linux:
      ```
      python -m venv .venv
      source .venv/bin/activate
      ```
3. Install dependencies
    ```
    pip install -r requirements.txt
    ```
4. Apply migrations
    ```
    python manage.py migrate
    ```
5. (Optional) Create a superuser
    ```
    python manage.py createsuperuser
    ```
6. Run the development server
    ```
    python manage.py runserver
    ```
7. Open the app in your browser:
    ```
    http://127.0.0.1:8000
    ```

## Project structure
```
/apps
  /authentication    # login, registration
  /home              # landing and main app logic
  /static            # static assets (css, js, images)
  /templates         # HTML templates
  __init__.py
  config.py
/core               # core Django project files
/media              # uploaded/processed files
/myenv              # environment scripts/config (optional)
.gitignore
db.sqlite3
manage.py
requirements.txt
runtime.txt
```

## Usage
- Register or log in via the authentication app (usually under `/apps/authentication`).
- Uploaded files are stored in `/media` — ensure MEDIA_ROOT and MEDIA_URL are configured in settings.
- Static assets served from `/static` during development; configure a static files server for production.
- Extend or replace apps following Django app conventions.

## Contributing
1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -am "Add feature"`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

Use GitHub Issues for bug reports and feature requests.

## Notes
- Review `config.py` and Django settings before deploying.
- For production, configure a proper DB, static/media hosting, and secure settings (SECRET_KEY, DEBUG=False).

## License
MIT — see `LICENSE` for details.
