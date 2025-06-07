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


6. Sample input data
a) For creating classes - POST /api/classes/

    {
       
        "name": "Yoga Basics",
        "date_time": "2025-06-08T15:30:00+05:30",
        "instructor": "ABC",
        "available_slots": 9,
        
      }

b) To get the Classes List - GET /api/classes/

   {
    "id": 1,
    "name": "Yoga Basics",
    "date_time": "2025-06-08T15:30:00+05:30",
    "instructor": "ABC",
    "available_slots": 9,
    "created_at": "2025-06-07T14:20:49.198560+05:30"
   }

c) For Booking the class - POST /api/book/

  {
    
    "client_name": "Shravani Kavale",
    "client_email": "shravani.kavale27@gmail.com",
    "fitness_class": 1
  }

d) To get the Booking List - GET /api/bookings/

  {
    "id": 1,
    "client_name": "Shravani Kavale",
    "client_email": "shravani.kavale27@gmail.com",
    "created_at": "2025-06-07T14:27:42.678939+05:30",
    "fitness_class": 1
  }

