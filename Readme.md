# Art portfolio app
The portfolio app is designed to showcase a (specific) paintings portfolio. It was designed 
so the user can modify image cate
to send alerts to a specific email whenever anyone fills a contact form.

### Install and use
* open a terminal
* create a virtual environment
* activate the virtual environment
* install requirements:
> pip install -r requirements.txt
* navigate to the location of manage.py ("core/manage.py")
* run the server
> manage.py runserver
* open your browser and navigate to http://localhost:8000/
* to use it as a superuser:
* (quit the server with Ctrl+Break)
* create a superuser
> manage.py createsuperuser
* run the server again
> manage.py runserver 
* open your browser and navigate to http://localhost:8000/admin
* log in to look at the database
* "Painting categories" holds the category name, description and image. Adding or removing a category
will dynamically add/delete a category on the homepage
* "Paintings" holds the painting name, description and image. Adding or removing a painting
will dynamically add/delete it.
* the app is supposed to send an email from a specific Gmail address to your email address.
The feature is currently disabled (therefore skipped) in views.py. To configure it, navigate to 
"core/TeenyTiny/sisiMailSender.py", go to the MailSender object. Make sure you have a gmail account that is configured
to work with Python. Follow the instructions in sisiMailSender.py
* even without an email to notify you of the changes, all form fills are captured in the "ReceivedEmails" model
 
### Features
* responsive
* can be configured by uer (up to an extent) 

### Quick wins
* the app can be easily converted in an e-commerce website by redirecting to a shop from
* the app can have a stock management side attached to it relatively easy for non-unique merchandise (prints, shirts)
* the app can be easily configured to create and track invoices