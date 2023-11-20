# jumpingmind-elevator-system

## Overview

This project implements a basic elevator system using Django and the Django REST Framework. The system includes models for floors, elevators, and user requests, providing APIs to initialize the system, manage elevators, handle user requests, and monitor elevator status.

## Table of Contents

- [Architecture](#architecture)
- [Repository File Structure](#repository-file-structure)
- [Database Modeling](#database-modeling)
- [Libraries and Dependencies](#libraries-and-dependencies)
- [API Contracts](#api-contracts)
- [Steps to Setup, Deploy, and Test](#steps-to-setup-deploy-and-test)

## Architecture

The system follows a simple client-server architecture. The backend is implemented using Django, providing a RESTful API for the frontend or client application to interact with.

## Repository File Structure

elevator_system/
|-- elevator_system/
| |-- settings.py
| |-- ...
|-- elevator/
| |-- models.py
| |-- serializers.py
| |-- views.py
| |-- urls.py
|-- README.md
|-- manage.py
|-- requirements.txt

- `elevator_system/`: Django project settings and configurations.
- `elevator_app/`: Django app containing models, serializers, views, and URLs related to the elevator system.

## Database Modeling

The system uses Django models to represent the data structure:

- `Floor`: Represents a floor in a building.
- `Elevator`: Represents an elevator with properties such as current floor, direction, door status, running status, and operational status.
- `UserRequest`: Represents a user's request for an elevator, including the associated elevator, floor number, and direction.

## Libraries and Dependencies

The project uses the following main libraries and dependencies:

- Django: Web framework for building the backend.
- Django REST Framework: Extension for building RESTful APIs with Django.

## API Contracts

### 1. Initialize Elevator System

**Endpoint:** `/initialize_elevator_system/`

**Method:** `POST`

**Parameters:**
- `num_elevators` (integer): Number of elevators to initialize.

### 2. Fetch Requests for Elevator

**Endpoint:** `/fetch_requests_for_elevator/`

**Method:** `GET`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 3. Fetch Next Destination

**Endpoint:** `/fetch_next_destination/`

**Method:** `GET`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 4. Fetch Elevator Direction

**Endpoint:** `/fetch_elevator_direction/`

**Method:** `GET`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 5. Save User Request

**Endpoint:** `/save_user_request/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.
- `floor_number` (integer): Requested floor number.
- `direction` (string): Direction of travel.

### 6. Update Elevator Status

**Endpoint:** `/update_elevator_status/`

**Method:** `PUT`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 7. Open Door

**Endpoint:** `/open_door/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 8. Close Door

**Endpoint:** `/close_door/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 9. Move Elevator Up

**Endpoint:** `/move_elevator_up/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 10. Move Elevator Down

**Endpoint:** `/move_elevator_down/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 11. Stop Elevator

**Endpoint:** `/stop_elevator/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 12. Mark Elevator Operational

**Endpoint:** `/mark_elevator_operational/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

### 13. Mark Elevator Non-Operational

**Endpoint:** `/mark_elevator_non_operational/`

**Method:** `POST`

**Parameters:**
- `elevator_id` (integer): ID of the elevator.

## Steps to Setup, Deploy, and Test

1. **Clone the Repository:**
git clone https://github.com/kumarr-amarr/jumpingmind-elevator-system.git
cd elevator-system

2. **Install Dependencies:**
pip install -r requirements.txt

3. **Run Migrations:**
python manage.py migrate

4. **Create Superuser :**
python manage.py createsuperuser

5. **Run Development Server:**
python manage.py runserver

6. **Access the API:**
Open a web browser and go to http://localhost:8000/ or use a tool like [curl](https://curl.se/) or [Postman](https://www.postman.com/) to interact with the API.

7. **Run Tests:**
test apis on given server on: http://localhost:8000/   (in my case ) using postman or on another platform by given JSON DATA in LINK:
https://api.postman.com/collections/19665212-a1083f0d-4bd7-4036-b354-c2bcb680736a?access_key=PMAT-01HFPC80VSNKS5DQ3ERJCYEYEM

or import elevator-system.postman_collection2 in postmen from "JSON_DATA" directory of this project