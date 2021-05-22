# Patient-Management-System

Patient-Management-System is a diagonostic management project developed in django. Admin can add doctor, add services, add gallery pictures . User can see doctors profile and also they can make appointment. They can also contact to the Patient-Management-System through email.

# To collect static files
```
python manage.py collectstatic
```
# Creating Superuser
To create superuser open terminal and type
```
python manage.py createsuperuser
```
# For email sending functionality fill up the information in Your Project setting
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password'
```
# To run the program in local server use the following command
```
python manage.py runserver
```
# Project snapshot

## Home page
![image](https://user-images.githubusercontent.com/19981097/57323709-0ea78180-7128-11e9-96f7-87dacdc8c0b8.png)

## Services Page
![image](https://user-images.githubusercontent.com/19981097/57323753-2979f600-7128-11e9-8c52-3b3ca47ffb12.png)

## Doctors Page
![image](https://user-images.githubusercontent.com/19981097/57323797-44e50100-7128-11e9-8ba9-caf1d433e359.png)

## Contact Page
![image](https://user-images.githubusercontent.com/19981097/57323832-562e0d80-7128-11e9-9c1e-235c300d084a.png)

## Appointment page
![image](https://user-images.githubusercontent.com/19981097/57323887-778ef980-7128-11e9-9a87-90d249a03577.png)

## Admin Panel
![image](https://user-images.githubusercontent.com/19981097/57323932-93929b00-7128-11e9-9dc0-ba53e5c9e1b1.png)

## Author
<blockquote>
Dipto Kumar Kundu
Email: dkkundu00@gmail.com
</blockquote>

========Thank You !!!=========




