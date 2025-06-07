# 🧘‍♀️ Yoga Class Booking API

A Django RESTful API to manage Yoga class schedules and client bookings.

## 📌 Features

- Create and view yoga classes
- Book available classes by client name and email
- Prevent double bookings and overbooking
- Timezone support for users
- View bookings (all or filtered by email)

---

## 🚀 Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (default)

---

## 🛠️ Setup Instructions

1. Clone the Repo

```bash
git clone https://github.com/shravanikavale/Yoga_BookingAPI.git
cd Yoga_BookingAPI

2. Create Virtual Environment
python -m venv venv
venv/Scripts/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Run Server
python manage.py runserver



