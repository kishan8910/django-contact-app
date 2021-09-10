Clone or download the repository
Run command cd django-contact-app/
Run command pip install -r requirements.txt
Run command python manage.py makemigrations
Run command python manage.py migrate
Run command python manage.py runserver
Go to any web browser and type the url (by default it would be http://127.0.0.1:8000/)
Now the home page of the app should be shown.
The user could uplaod file with data and that would insert the customer details to the database and it would show the details in the same page. (an example file is created along with this project 'test.xlsx')



For testing the upload using Postman
Open postman
Create a new POST request (the url should be http://127.0.0.1:8000/import)
In body, choose form-data
Add a key value pair (key should be excel_file and value should be file uplaod)
Select the file from the local system and send the request (an example file is created along with this project 'test.xlsx')

