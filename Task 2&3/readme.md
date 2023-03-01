
#steps follows to create a project :
  1)Run the following command to create a new Django project: ** django-admin startproject myproject **
    This creates a new directory called myproject that contains the basic files and directories for a Django project.
  2)command to create a new Django app called blog:  ** python manage.py startapp blog **
    This creates a new directory called blog that contains the files and directories for the blog app.
  3)Open the models.py file in the blog app directory and add the following code to define the **Post** and **Author** models:
  4) after that Open the admin.py file in the blog app directory and register the **Post** and **Author** models with the admin site:
  5)Run the following command to create a new database for the project: **python manage.py migrate**
  6)start the development server: **python manage.py runserver**
  7)Open the views.py file in the blog app directory and make your view:
  8)Open the urls.py file in the blog app directory and define a URL pattern for the views:
  9)start server : **python manage.py runserver**



