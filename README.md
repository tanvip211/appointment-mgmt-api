Appointment Management API

Project Overview

The Appointment Management API is a backend application built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic. It allows customers to book appointments with service providers based on available time slots. It ensures proper validation and avoids scheduling conflicts.

This project was created for the Gen AI Training Assignment. It demonstrates backend API development, database integration, and appointment scheduling logic.

Features

Customer Management (Create, Read, Update, Delete)
Service Provider Management (Create, Read, Update, Delete)
Time Slot Management (Create, Read, Update, Delete)
Appointment Management (Create, Read, Update, Delete)
Appointment Booking
Appointment Cancellation
Appointment Rescheduling
Double Booking Prevention
Search Appointments by Customer
Search Appointments by Provider
Search Appointments by Date
Pagination Support
Request Validation using Pydantic
Interactive Swagger Documentation
Database Migration Support using Alembic


Technology Stack

FastAPI
PostgreSQL
SQLAlchemy ORM
Alembic
Pydantic
Uvicorn



Project Structure

appointment-mgmt-api/
-> app/
--> api/
--> core/
--> models/
--> schemas/
-> create_tables.py
-> main.py
-> alembic/
--> versions/
-> .env.example
-> alembic.ini
-> README.md



Database Entities

Customer

Stores customer information.

Fields:

id
name
email
phone

Provider

Stores service provider details.

Fields:

id
name
email
specialization

TimeSlot

Stores available appointment slots.

Fields:

id
provider_id
start_time
end_time

Appointment

Stores appointment booking information.

Fields:

id
customer_id
provider_id
timeslot_id
status

API Endpoints

Customers

GET /customers
GET /customers/{id}
POST /customers
PUT /customers/{id}
DELETE /customers/{id}

Providers

GET /providers
GET /providers/{id}
POST /providers
PUT /providers/{id}
DELETE /providers/{id}

Time Slots

GET /timeslots
GET /timeslots/{id}
POST /timeslots
PUT /timeslots/{id}
DELETE /timeslots/{id}

Appointments

GET /appointments
GET /appointments/{id}
POST /appointments
PUT /appointments/{id}
DELETE /appointments/{id}
PUT /appointments/{id}/cancel
PUT /appointments/{id}/reschedule
GET /appointments/search
GET /appointments/search-by-date

Setup Instructions

1. Clone Repository

git clone <repository-url>
cd appointment-mgmt-api


2. Create Virtual Environment

python -m venv venv


3. Activate Virtual Environment

venv\Scripts\activate


4. Install Dependencies


pip install -r requirements.txt


5. Configure PostgreSQL

Create a PostgreSQL database:


appointment_db


Update database credentials in:


app/core/database.py


6. Run Application


uvicorn app.main:app --reload


7. Access Swagger Documentation


http://127.0.0.1:8000/docs

NOTE: The databse schema diagram is added in docs folder.

BY:
Tanvi Panchal
Gen AI Training Assignment
