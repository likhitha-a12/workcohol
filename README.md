# Event Management System

This repository is a Django-based Event Management System designed to help users browse, book, and manage a variety of events. The platform provides user registration, event listing, booking with payment, and a contact form for inquiries.

## Features

- **User Registration & Login:** Secure authentication for users.
- **Event Listing:** Browse and view details of available events.
- **Event Booking:** Book events with detailed forms and payment options.
- **Admin Panel:** Manage events, bookings, and users via Django admin.
- **Contact Form:** Users can send inquiries directly from the website.
- **Responsive Design:** Modern UI with Bootstrap and custom CSS.

## Project Structure

```
.
├── eventapp/                # Django app for event logic (models, views, serializers)
├── eventpr/                 # Django project settings and URLs
├── userapp/                 # User management app
├── static/                  # Static files (CSS, JS, images)
├── template/                # HTML templates
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── data.json                # Sample data (if any)
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.12.10
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/likhitha-a12/workcohol.git
   cd workcohol-main
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the application:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

- Register as a user or log in.
- Browse available events.
- Book an event and receive a confirmation email.
- Contact the team via the contact form.
- Admins can manage events and bookings via `/admin`.

## License

This project is licensed under the MIT License.

---

**Note:** Update the repository URL and project details as needed.