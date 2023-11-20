# jumpingmind-elevator-system
1. chose a directory to clone this repository

2. best pratice use it by creating a virtual environment using --> py -m venv name_of_virtual_invironment (in my case elevator-system-virtyal-environment)

3. activate virtual env using --> name_of_virtual_invironment\scripts\activate.bat

4. Install Django --> pip install django

5. Install Django rest framework --> pip install djangorestframework

6. now switch to project in cmd and run:
    i. py manage.py makemigrations
    ii. py manage.py migrate
    iii. py manage.py runserver

7. test apis on given server on: http://localhost:8000/   (in my case ) using postman or on another platform by given JSON DATA in LINK:
https://api.postman.com/collections/19665212-a1083f0d-4bd7-4036-b354-c2bcb680736a?access_key=PMAT-01HFPC80VSNKS5DQ3ERJCYEYEM

or import elevator-system.postman_collection2 in postmen from "JSON_DATA" directory of this project