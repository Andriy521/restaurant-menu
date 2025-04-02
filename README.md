# Restaurant Menu

## Description
Restaurant Menu is a Django-based web application that allows restaurant owners to manage their menus efficiently. It provides a user-friendly interface to add, edit, and remove menu items while ensuring a clean and minimalistic design with a dark theme.

## Features
- Add, edit, and delete menu items
- Categorize dishes for easy navigation
- Dark-themed, minimalistic design with Bootstrap 5
- Secure user authentication (optional)
- Responsive UI for desktop and mobile devices

## Installation

### Prerequisites
- Python 3.x
- Virtual environment (recommended)
- PostgreSQL or SQLite (default)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant_menu.git
   cd restaurant_menu
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add the following variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to manage the application:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create a superuser account.

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Navigate to `http://127.0.0.1:8000/`
- Start managing your restaurant’s menu

## Demo
- Navigate to `https://restaurant-menu-fp6l.onrender.com`
- use demouser
  ```bash
   login: user
   password: user12345
   ```