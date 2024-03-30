#DJANGO STEPS
#Is a python web framwork(means is is procedual) that we use to create web applications
#Django is extremely procedual(step by step),it follow an MVC model(model,view,controller)
# Examples of python frameworks
#     1.django
#     2.flask
#     3.pyramid
#     4.py2web
# we use methods to capture data
#we will have files for view.py that will handle the database and views display
#models are files that are managing data bases
#views are file that will be handling the models and requests-model.py
#A model is a database table(modules)-is where our manipulation of data is going to be done

#controllers are th urls-therefore we will create files for the urls which will be conncected with the requests

#Any url e.g mtn.co.ug,mtn.co.ug/register must be served by one or more views or functions meaning any url item or list item must

#views and urls directly connects but its not a must for views to directly connect with database

#In a database you can have one or more tables

#HOW TO INSTALL DJANGO
#we created a djangofolder-mkdir my_project
#we cd my_project
#we installed django using pip install django
#we then checked by typing python the import django.
#we are now gona create a django project
#input in terminal djnago-admin start project First project
#checked the servers opened each template
#Ran our terminal cd my project
#then cd First_project
# then python manage.py runserver.
#copied the http://file- http://127.0.0.1:8000/ and pasted it in the browser to see if django is working
#yes its working


#then we migrate->python manage.py migrate
#>python manage.py runserver
#the copy the http://127.0.0.1:8000/admin

#THE STRUCTURE OF DJANGO
#django has a project ...in yoh project ia where there is yoh website/overall container of yoh web application
#django comes with database and server
"""
C:\Users\PC\Desktop>cd My_project

C:\Users\PC\Desktop\My_Project>cd First_project

C:\Users\PC\Desktop\My_Project\First_project>manage.py migrate

C:\Users\PC\Desktop\My_Project\First_project>
manage.py migrate

C:\Users\PC\Desktop\My_Project\First_project>
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

C:\Users\PC\Desktop\My_Project\First_project>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 28, 2024 - 21:44:32
Django version 5.0.3, using settings 'First_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[28/Mar/2024 21:45:03] "GET / HTTP/1.1" 200 10629
[28/Mar/2024 21:45:11] "GET /admin HTTP/1.1" 301 0
[28/Mar/2024 21:45:11] "GET /admin/ HTTP/1.1" 302 0
[28/Mar/2024 21:45:11] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4158
[28/Mar/2024 21:45:11] "GET /static/admin/css/base.css HTTP/1.1" 200 21544
[28/Mar/2024 21:45:11] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17905
[28/Mar/2024 21:45:11] "GET /static/admin/css/login.css HTTP/1.1" 200 958
[28/Mar/2024 21:45:11] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[28/Mar/2024 21:45:11] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2682
[28/Mar/2024 21:45:11] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[28/Mar/2024 21:45:11] "GET /static/admin/js/theme.js HTTP/1.1" 200 1943

"""