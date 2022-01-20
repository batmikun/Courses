# DJANGO

# Is a way to build web applications

# DJANGO TERMINOLOGY

# Project is a collection of applications
# Our project is "dj4e-sample"
# Porject-wide configuration is in dj4e-samples/dj4e-samples

# Our first application is "hello"
# We will do most of our web development in the application folder dj4e-samples/hello

# FOLDER STRUCTURE

# Project
# __init__.py
# settings.py
# urls.py
# wsgi.py

# Application
# __init__.py
# admin.py
# apps.py
# migrations
# models.py
# tests.py
# urls.py
# views.py

# FLOW OF A WEB REQUEST

# When the request arrives at a Djando app the incoming request URL is compared to the list of paths in
# urls.py in the variable urlpatterns

# When there is a url match, it selects a "view" which is a bit of code that handles any database access and then produces
# and delivers the response to the browser

# The view access the database indirectly through an abstraction called a "model"

# This is a general web pattern called "Model-View-Controller" or MVC.

# VIRTUAL HOSTING

# Virtual Hosting - Many domains on one system
# HTTP - Hypertext Transport Protocol
# Connects to a domain
# Includes the domain in the GET request

# HTML - Hypertext Markup Language

# A way of marking up text to indicate that some text is different than other text
# We "tag" portions of the text to communicate meaning.

# Always starts with
#
#
# <html>
#   <head>
#   </head>
#
#   <body>
#   </body>
# </html>
#

# SPECIAL FILE NAMES
# When a URL points to a directory in your web server, it looks
# for a file with a special name.
# index.html, index.htm, index.php, etc.
# While there is a convention, the "default file" is configurable -
# so nothing is "sure".
# Usually index.htm or index.html is a safe bet
# This only works when viewing through a web server - when viewing from disk, you must view the file

# MULTIPLE FILES
# We can put multiple files in the same directory and links the with relative links

# Absolute Link : Contains the full url with protocol
# Relative Link : It is implied that the document is in the same server

# Important Tags

# <a href="">Clickeable Part</a>

# <img src="">

# <ul> Unordened List
#   <li></li>
#   <li></li>
# </ul>

# <table>
#   <thead>
#       <tr>
#           <th></th>
#       </tr>
#   </thead>
#  <tbody>
#       <tr>
#           <td></td>
#       </tr>
#   </tbody>
# </table>

# <p>Paragraph</p>
# <pre>Preformatted</pre> # This respects spaces and jump lines.

# CSS - Cascading Style Sheets

# CSS is a set of "rules" which in include a "selector" and one
# or more "properties" and "values" as well as some punctuation

# body {
#   font-family: arial, sans-serif;
# }

# selector {
#   property: value;
# }

# selector => we have the tag selector tagname {}, that styles a tag accross the whole document
# selector => we have the class selector .classname {}
# selector => we have the id selector #idname {}

# #idname p {} afecta a todos los tag <p> dentro del <div id="idname">.
# .classname p {} afecta a todos los tag <p> entro del <div class="classname">.

# we can apply css in different ways :

# inline - right on an HTML tag - using the style = "attribue;"
# inside a style tag - <style> body {} </style>. This tag is like the <script> tag.
# external - in a file called style.css and call inside the header of the html

# the css is in order of specificity. If we affect the body, from a external file, but we
# have a inline style in the tag body, the inline style takes priority and override the external css.
# It reads from top to bottom. But the priority is to the contrary, from bottom to top.

# SPAN AND DIV TAGS
# <span> and <div> are two different tags.
# <span> in a inline tag, no deffault style associated.
# <div> is a block tag, that has no deffault style associated.

# Messaurment units

# px = pixeles
# em = the width of the font, especially the letter m or e ?)
# fr = fraccion
# % = porcentaje

# <br clear="all"> => clear the floats

# Colors = aqua, black, blue, fuchsia, gray, green,
#          lime, maroon, navy, olive, purple, red, silver
#          teal, white, yellow. This are the colors that can be used by name.

# The best way and the most used one is the hexadecimals.

# Hexadecimal = #RRGGBB
# RGB => rgb(red, green, blue)

# font-family: arial, sans-serif; Most Favorite (special font, downloaded font, etc) -> Less Favorite (fallback font)
# fallback fonts: serif, sans-serif, monospace. cursive and fantasy
# font-weight: normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900
# font-style: normal, italic, oblique
# font-size: xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger
# font-variant: normal, small-caps
# text-decoration: none, underline, overline, line-through, blink

# CSS BOXES

# Block tags like div p and h1 live in a "Box". Working from the inside out you have:

# 1) The text or image content wrapped as appropriate taking up horizontal and vertical space
# 2) The padding is the space between the content and the border and is colored the same as the text
# 3) The border has its own color and width.
# 4) The margin is the space between the border and the rest of the elements in the document.

# To keep the overflow from happening in boxes that are to tiny, or whatever.
# we use the overflow property => overflow: hidden; or overflow: visible; or overflow: scroll; or overflow: auto;  (default)

# POSITIONING

# 1) By default the boxes follow after each other
# 2) Relative => The box is positioned relative to the parent box
# 3) Absolute => The box is positioned relative to the document
# 4) Fixed => The box is positioned relative to the viewport

# z index => The z-index property specifies the stack order of an element.

# UL

# line-style-type: none; Remueve los redondelitos

# LI
# display: inline-block; # Para que quedem em una linea

# Install ngrok

# This allows you to see your localhost in a temporary domain in the real world
# This is usefull to see a preview of your site in a "production enviroment"

# SQL => Structured Query Language

# Is the language we use to issue commands to the database
# - Create - CREATE TABLE nameoftable(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(128), etc )
# - Insert Data - INSERT INTO table(fields) VALUES (values)
# - Read/Select some data -  SELECT * FROM table WHERE
# - Update Data - UPDATE table SET field="value" WHERE
# - Delete Data - DELETE FROM table WHERE
# - Order - ORDER BY field ASC/DESC (Only for SELECT)

# RELATIONAL DATABASE

# Relational databases model data by storing rows and columns in tables.
# The power of the relational database lies in its ability to efficiently
# retrive data from those tables and in particular where there are multiple
# tables and the relationship between those tables involved in the query.

# Four major Database Management Systems in wide use
# - Postgress - Open Source, enterprise-scale, very tweakable
# - Oracle - Large, commercial, enterprise-scale, very tweakable
# - Mysql - Simpler bet very fast and scalable. Commercial open source
# - SqlServer - Very nice - From Microsoft
# Samaller Projects
# - SQLite
# - HSQL

# DATABASE MODEL

# A database model or database schema is the structure or format of a database,
# described in a formal language supported by the database management system.
# In other words, a "database model" is the application of a data model when used in conjunction
# with a database management system.

# Object Relational Mapping (ORM) - Doctrine, Eloquent, etc.

# Allos us to map tables to objects and columns
# We use those objects to store and retrieve data from the database
# Improved portability across database dialects (SQLite, MySQL, Postgres)

# SQL;

# CREATE TABLE Users {
#   name VARCHAR(128) NOT NULL,
# }

# models.py

# from django.db import models

# class User(models.Model) :
#   name = models.CharField(max_length=128)


# Migrations

# python manage.py makemigrations => The makemigrations command reads all the models.py files in all the applications
# and creates a migration file for each model. If you make a new application you have to register it in settings.py

# python manage.py migrate

# python3 manage.py shell

# from usermodel.models import User
# u = User(name='John')
# u.save()
# print(u.id)
# print(u.name)

# from django.db import connection
# print(connection.queries) => shows a little bit of debugging data

# CRUD

# SAVE

# u.save()

# SELECT

# User.objects.values() # .values() execute the query
# User.objects.filter(name='John').values()

# DELETE

# User.objects.filter(name='John').delete()

# UPDATE

# User.objects.filter(name='John').update(name='John')

# ORDER_BY

# User.objects.values().order_by('name') (ASC)
# User.objects.values().order_by('-name') (DESC)

# MODEL FIELD TYPES

# AutoFiled, BigAutoField, BigIntegerField, BinaryField, BooleanField,
# CharField, DateField, DateTimeField, DecimalField,
# DurationField, EmailField, FileField, FilePathField, FloatField,
# ImageField, IntegerField, GenericIPAddressField,
# NullBooleanField, PositiveIntegerField,
# PositiveSmallIntegerField, SlugField, SmallIntegerField,
# TextField, TimeField, URLField, UUIDField
# ForeignKey, ManyToManyField, OneToOneField


# REQUEST FLOW

# B => Request => Routing <== urls.py
# R              |
# O              |    <=> views.py
# W            Views  ===========> Templaste
# S <== Rsp <==  |    <=> forms.py ====>|^
# E              |<-------->|^
# R              |        Models <=> Database
#              Shell   <==  |
#                           |  <==   models.py
#              /admin  <==> |           |
#                 |                     |
#              admin.py <---------------|

# urls.py controller
# Views.py some acts like a controller or like a template
# Models.py all the work to talk to the database

# M - We call the Data bit - the "Model" or Data Model
# V - We call the "making the next HTML" bit the "View" or "Presentation Layer"
# C - We call the handling of input and general orchestration of it all the "Controller"


# VIEWS AND TEMPLATES

# Views are the core of our application
# Django looks at the incoming request URL and uses urls.py to select a view
# The view from views.py
# Handle any incoming data in the request and copy it to the databa through the model
# Retrieve data to put on the page from the databa through the model
# Produce the HTML that will become the response and return it to the browser

# Reading the URL

# When Django  an HTTP request it parses it, uses some of the URL for routing purposes
# and passes parts of the URL to your code

# https://samples.dj4e.com/views/funky => views is part of the Django application (also folder)
#                                      => funky is the view within the application

# URL DISPATCHER => Lo que esta encargado de hacer el routing

# Three patterns for defining views

# 1 - Requests are routed to a pre-defines class from Django itself
# 2 - Requests are routed to a function in views.py that takes the http request as a parameter and returns a response
# 3 - Requests are routed to a class in views.py that has get() and post() methods that take the http request as a parameter and return a response

# 1 - path('', TemplateView.as_view(template_name='views/index.html'),
# 2 - path('funky', views.funky)  path('rest/<int:guess>', views.rest) => int -> tipo de dato esperado, guess => nombre q le ponemos al parametro
# 3 - path('main', views.MainViews.as_view()) | path('remain/<slug:guess>', views.RestMainView.as_view())

# Templates => views/templates/views/main.html

# Request and Response Objects

# Django uses request and response objects to pass information throughout your Django Application
# When a page is requested by a browser, Django create an HttpRequest object that contains metada about the request
# The Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is resposible for returning an HttpResponse object.
# The application programming interfaces (APIs) for HttpResquest and HttpResponse objects, are defined in the django.http module

# Class HttpRequest

# Attributes
# All attributes should be considered read-only, unless stated otherwise

# HttpRequest.schema
# A string representing the scheme of the request (http or https)

# HttpRequest.body
# The raw HTTP request body as a bytestring. This is useful for processing data in different ways than
# conventional HTML forms: binary images, XML payload etc. For processing conventional form data,
# use HttpRequest.POST

# There are like 20 more attributes in the object Response

# Class HttpResponse

# In contrast to HttpRequest objects, which are created automatically by Django. HttpResponse objects are your responsibility to create.
# Each view you write is responsible for instantiating, populating, and returnin an HttpRepsonse

# Passing strings
# Typical usage is to pass the contents of the pafe, as a string or bytestring, to the HttpResponse constructor.

# VIEW EXAMPLE
# views/funky
# from django.http import HttpResponse
# from django.httl import HttpResponseRedirect
#
#
# def funky(request):
# response = """<html><body><p>Hola</p></body></html>"""
# return HttpResponse(response)

# def danger(request):
#   getQueryString = request.GET.get('q')
#   response = """<html><body><p>""" + getQueryString + """</p></body></html>"""
#   return HttpResponse(response)

# I use the django.http.escape() function whenever i sense danger...

# It is dangerous to take data from the user and include it in the HTTP Response without "escaping" the output
# HTML + Javascript is a programming language and you don't want your users "sending code" to other user's browsers

# Investigate Cross-Site Scripting

# To avoid Cross-Site Scripting, if we use query params we have to encrypt the data
# We can use django.http.escape() to encrypt the data

# from django.utils.html import escape
# escape(request.GET('q'))

# Class Views - Inheritance

# path('main', views.MainViews.as_view()) When we use as_view, inside our MainView file/function we have to have a method Get or Post. Django handles wich picks based on the method of the request.

# from django.http import HttpResponse
# from django.utils.html import escape
# from django.views import View

# class MainView(View):
#   def get(self, request):
#       return HttpResponse("<html><body><p>Hola</p></body></html>")

# HTTP Location Header
# You can send a "Redirect" reponse instead of a page response to communicate a "location:" header to the browser.
# The location header includes a URL that the browser is supposed to forward itself to
# It was originally used for web sites that moved from one URL to another.

# Sending a Redirect from a View

# return HttpResponseRedirect('AbsoultePathURL')


# Templates in Django

# Being a web framework, Django needs a convenient way to generate HTML dynamically. The most
# common approach relies on templates. A template contains the static parts of the desired HTML
# output as well as some special syntax describing how dynamic content will be inserted.

# A django project can be configured with one or several template engines (or even zero if you don't use templates).
# Django ships built-in backends for its own template system, creatively called the Django template language(DTL), and
# for the popular alternative Jinja2.

# A template is simply a text file. It can generate any text-based format (HTML, XML, CSV, etc).
# A template contains variables, which get replaced with values when the template is evaluated,
# and tags, which control the logic of the template.

# Template Render Process


# {'dat' : 'Hola'}                   <h1> {{ dat }} </h1>
#
# Render Data => [ Render Engine ] <== Template
#                       |
#                 Rendered Output
#
#                 <h1> Hola </h1>

# path('game/<slug:guess>', views.GameView.as_view())

# from django.shortcuts import render
# from django.views import View

# class GameView(View):
#   def get(self, request, guess):
#       x = {'guess' : int(guess)}
#       return render(request, 'tmpl/cond.html', x) => render(request, 'templatenamespace', context)

# A django project is made of one or multiple applications.
# We use "namespace" so that each application can load its own templates

# favs/templates/favs/detail.html
# We have to repite the name of the application because the templates are global accross all the project
# so when we call a template we have to do it 'appname/template_name'

# Template Tags

# Substitution {{ variable }} this things have modifiers that we can use
# {{ variable|escape }}
# {{}} => does the escape automatically
# If we want not to escape a variable, we use {{ variable|safe }}

# Calling mode
# {% url 'cat-detail' cat.id %}
# {% author.get_absolute_url %}

# Logic
# {% if variable %}
# {% endif %}

# Blocks
# {% block content %}
# {% endblock %}

# Loops
# {% for variable in list %}
# {% endfor %}

# def loop(request):
#   f = ['Apple', 'Orange']
#   n = ['peanut', 'cashew']
#   o = {'inner' : '42'}
#   x = {'fruit' : f, 'nut' : n, 'outer' : o}
#   return render(request, 'tmpl/loop.html', x)

# Template Inheretance

# When we make a new template - we can extend an existing template and the add
# our own little bit to make our new class

# Another form of store and reuse

# DRY (Don't Repeat Yoursel)

#                  Base Template
#                       |
# Render Data => [ Render Engine ] <== Template
#                       |
#                 Rendered Output

# tmpl/template/tmpl/base.html
# <html>
#   <head>
#       <title>Base template</title>
#   </head>
#   <body>
#       {% block content %}{% endblock %}
#   </body>
# </html>

# tmpl/template/tmpl/cond.html
# {% extends 'tmpl/base.html' %}
# {% block content %}
#   <h1>Hola</h1>
# {% endblock %}

# Reverse Resolution of URLs
# A common need when working on Django project is the possibillity of obtain URLs in thier final forms either
# for embedding in a generated content of for handling of the navifation flow on the server side(redirections, etc)

# It is strongly desirable to avoid hard-coding these URLs. Equalli dangerous is devising ad-hoc mechanisms to generate
# URLs that are parallel to the design described by the URLconf, which can result in the production of
# Urls that become stale over time

# In other words, what's needed is a DRY mechanism. Among other advantages it would allow evolution of the
# URL design without having to go over all the project source code to sarch and replace outdated URLs.

# The primary piece of information we have available to get a URL is an identification (e.g the name) of the view
# in charge of handling it. Other pieces of information that necessarily must participate in the lookup of the right
# URL are the types (positiona, keyword) and values of the view arguments

# urls.py
# urlpatterns = [
#   path('', TemplateVies.as_view(), name='route/home.html'),
#   path('about', views.FirstView.as_view(), name='first-view'),
# ]

# <li>
#   <a href="/route/second"> HARD CODE URL
# </li>
# <li>
# {% url 'route:first-view' paramter %}
# </li>
# <li>
# <a href="{% url 'route:second-view' %}"></a> -CORRECT WAY
# </li>

# {% url 'applicatioName:viewName' parameter %}

# In the project urls.py, instead of name we use namespace (we can use it of not)
# urlpatterns = [
#   path('/home', include('application.urls'), namespace='route/home.html'),
#   path('/oauth', include('oauth.urls'), namespace='first-view'),
# ]

# Other way of call urls in a view, is forming the urls in the controller

# from django.urls import reverse, reverse_lazy
# class SecondView(View):
#  def get(self, request):
#    u = reverse_lazy('application:view', parameter)
#    u3 = reverse('application:view', parameter)

# reverse_lazy and reverse is what django uses in the background when you call {% url () %}

# Built-in class-based generic views

# Writing web applications can be monotonoues, because we repeat certain patterns again and again.
# Django's generic views were developed to ease that pain. They take certain common idioms and patterns found
# in view development and abstract them so that you can quickly write common views of data without having to write
# too much repetitive code.

# We can recognize certain common tasks, like displaying a list of model objects, and write code that displays a list of any model object.
# Django ships with generic views to display list and detail pages for a single model object.

# Three diferent ways of doing the same thing

# class CatListView(View): # This is how we do it if we are not going repeat ourselves
#   def get(self, request):
#       stuff = Cat.objects.all()
#       c = {'cat_list' : stuff}
#       return render(request, 'gview/cat_list.html', c)

# class DogListView(View): # This code is more generic and this makes it more reusable
#   model = dog
#   def get(self, request):
#       modelname = self.model._meta.verbose_name.title().lover()
#       stuff = self.model.objects.all()
#       c = {'modelname+'_list' : stuff}
#       return render(request, 'gview/'+modelname+'_list.html', c)

# The dog class explains in depth what is happening with the horse view
# from django.views import generic
#
# class HorseListView(generic.ListView): # This is the same that the DogListView, with one line
#   model = horse

# generic.ListView is what have a similar code that the DogListView and because we inhereting
# from it we can use the same code to display a list of any model object

# Form

# Forms gather data and send it to the server

# Basic method -> GET and POST

# GET - Parameters are placed on the URL which is retrieved
# POST - The URL is retrieved and parameters are appended to the request in the HTTP connection.

# HTML 5 Input types

# text
# password
# email
# url
# number
# date => datepicker
# datetime
# time
# checkbox
# radio
# select
# multiple select
# textarea
# color => colorpicker
# url

# CSRF (Cross-Site-Request-Forgery)

# Attack
# A rogue site generates a page that includes form that posts data to a ligitimate site where the user is logged in via a session cookie
# The form is submitted to the ligitimate site and the cookie is include
# The ligitimate site accepts the request because of the cookie value
# Note that the rogue site does not nned to know the cookie value - it just knows that the cookie will be sent on
# request to the ligimate site

# Defense
# The ligitimate site chooses a large random number (CRSF Token) and puts it in the session
# When the ligitimate site generates a POST form, it includes the CSRF Token as a hidden input field
# When the form is submitted the CSRF Token is sent as well as the cookie
# The site looks up the session and rejects the request if the incoming CSRF Token does not match the session's CSRF Token

# To implement CSRF in Django

# from django.middleware.csrf import get_token

# def csrfform(request):
#   response = """ <input type="hidden" name="csrfmiddlewaretoken" value="__token__" """
#
#   token = get_token(request)
#   response = response.replace('__token__', html.escape(token))
#   response += dumpdata('POST', request.POST)
#   return HttpResponse(response)

# The easy way to implement CSRF in Django is using the tag
# {% crsf_token %} in the template

# POST - Refresh

# Once you do a POST a receive 200 status + a page of HTML, if you tell the browser to refresh,
# the browser will re-send the POST data a sacend time.
# Thhe user gets a browser pop-up that tries to explain what is about to happen

# DON'T ALLOW DOUBLE POSTS

# Typically POST requests are adding or modifying data whilst GET requests view data
# It may be dangerous to do the same POST twice (say withdrawing funds from a bank account)
# So the browser insists on asking the user (out of your control)
# Kind of an ugly UX / bad usability
# As developers we work so this never can happen

# POST-REDIRECT-GET-REFRESH [The solution
#
# Cookies [Browser] & Session [Server] => The session needs the cookies


# Multi-User / Multi-Browser
#
# When a server is interacting with many different browsers at the same time, the server needs to know *which* browser
# a particular request came from
# Request/ Response initially was stateless - all browsers looked identical. This wwas really bad and did not last very long at all

# Web Cookies to the Rescue
#
# Techbically, cookies are arbitrary pieces of data chosen by the Web server and sent to the browser.
# The browser returns them unchanged to the server, introducing a state (memory of previous events) into otherwise
# stateless HTTP transactions.
# Without cookies, each retrieval of a Web page or component of a Web page is an isolated event, mostly unrelated to all
# other views of the pages of the same site

# Cookies are part of the header of the response
# In django we can do this to set the cookies

# def cookie(request):
#   print(request.COOKIES)
#   response = HttpResponse('Hi')
#   response.set_cookie('name', 'value')
#   response.set_cookie('name', 'value', max_age=seconds_util_expire)
#   return response

# DJANGO SESSIONS

# Sessions are a way to store data on the server
# We can store like "this is user is logged in"
# In most server applications, as soon as we start a session for a new (unmarked) browser we create a session
# We set a session cookie to be stored in the browser. which indicates the session id in use - gives this browser a unique "mark"
# The creation and destruction of sessions is handled by a Django middleware that we use in our applications.

# With the cookie we create a session and that session is attached to the request object
# There can be as many cookies as distintc browser.

# Default - Store Sessions in the Database
#
# Browser [Cookie = A123], Browser[Cookie = B123]
# Session [A123], Session [B123]

# def sessfun(request):
#      num_visits = request.session.get('num_visits', 0) + 1
#      request.session['num_visits'] = num_visits
#      if num_visits > 4: del(request.session['num_visits'])
#      return HttpResponse('Your number of visits is %s' % num_visits)

# DATA MODELLING

# Model Desing
# Our goal is to avoid the really bad mistakes and design clean and easily understood models
# Starts with a sample data set and draws a picture

# Linking Field Types
# Foreign Key
# ManyToManyField
# OneToOneField

# 3 Rules For Databases
#
# Do not replicate string data - reference data - point at data
# Add a special "unique key" column to each table which we will make references to. What is know as id
# User integers for to make links between tables - integers are fast and small
# AVOID VERTICAL REPLICATION

# Legend :
#
# 1 One
# 1..* Many with a minimum of 1
# 0..* Many with a minimum of 0


# ONE TO MANY - Foreing Key
# In this relationship the nametable_id are in the side of the Many.
# The nametable_id is the foreign key in the Many table

# from django.db import models

# class Lang(models.Model):
#     name = models.CharField(max_length=200)
#
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     lang = models.ForeignKey('Lang', on_delete=models.SET_NULL, null=True)
#
# class Instance(models.Model):
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)
#     due_back = models.DateField(null=True, blank=True)
#
#
# About on_delate
# What do we do when a row in one table points to a row in a "foreign" table via a forgign key and the "destination row" is deleted
# on_delete = set_null Keep the row but set foreign key to null
# on_delete = cascade - Delete the row

# Demo Batch Loading from CSV

# Loading Data From a File
#
# Sometimes we need to pre-load data into our Django Databa
# This data might come from an API or file
# We need to write a Python program to function like the Django shell
# For this we need to instal pip3 install django-extensions
# And we need to modify the settings.py to add this extension
# INSTALLED_APPS = [
#   'django_extension',
# ]
#
# Make a scripts folder
# mkdir scripts
# touch scripts/__init__.py
#
# We place empty __init__.py files in folders to indicate to Python that they
# contain files that hold modules and as such are suitable for importing into
# a Python application

# Example
#
# import csv
# from cats.models import Cat, Breed
#
# def run():
#    fhand = open('cats/meow.csv')
#    reader = csv.reader(fhand)
#    next (reader) # Advance past the header
#
#    Cat.objects.all().delete()
#    Breed.objects.all().deleta()
#
#    # Name, Breed, Weight -> This is how it looks the csv file
#
#    for row in reader:
#        print(row)
#        b, created = Breed.objects.get_or_create(name=row[1]) => b is the variable where the Breed stores, and created returns true or false depending on if the object is new or not. This is a particular feature of the method get_or_create
#        c = Cat(nickname=row[0], breed=b, weight=row[2])
#        c.save()
#
# To run a script we hace to do
# python3 manage.py runscript name_of_the_script
#
# Login and Logout
#
# User authentication in Django
# Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions.
# The authentication system cosist of:
#
#     Users
#     Permission: Binary flags designating whether a user may perform a certain task.
#     Groups: A generic way of applying labels and permissions to more than one user.
#     A configurable password hashing system
#     Forms and view tools for logging in users, or restricting content
#     A pluggable backend system
#
# Authentication support is bundled as a Django contrib mudle in django.contrib.auth. By default, the required configuration
# is already included in settings.py
#
# Making the super user
# We need to "bootstrap" our system and make a user that can log into the adming page and make more users
#
# python3 manage.py createsuperuser
#
# Sessions are not "logging in"
# A session is a way of marking a browser and storing data on the server which can be stored an retrieved across
# multiple request-response-cycles
# Sessions exist irrespective of wheter or not the user is logged in
# When the user passes the login check. the server adds data to the session identifying the user
# When the user logs out, that information in the session is removed
# Sessions are required to implement login
# ISTALLED_APPS = [
#   'django.contrib.auth'
# ]
#
# We need to add a path to the code that gives us login and logout urls
# We can reverse lookup these urls susing the 'login' and logout' view names
# ulrpatter = [
#   path('accounts/', include('django.contrib.auth.urls')),
# ]
#
# To lookup these 'login/logout' url we can use the command reverse
# reverse('login') , reverse('logout')
#
# We want to transfer the user to a login page from many pages in our application and when they successfully log in, we want to bing
# them back to our page or some other page
#
# The "next=" parameter tells login or logout where yo redirect the user after login
#
# <a href="{% url 'logout'  %}?next={% url 'authz:open'  %}"
# <a href="{% url 'logout'  %}?next={{ request.path }}" => request.path = $this->referer()
#
# Look and Feel - Login Template
#
# To allow us to control the look and feel of the login page we must provide a template called "registration/login.html"
# Django describes what needs to he in this template
# we can put this in any of our application templates folder
#
# To deal with error
#
# {% if form.errors %}
#   <p>Your username and password didn't match</p>
# {% endif %}
#
# {% if next %}
#     {% if user.is_authenticated %}
#        <p>Your account doesn't have access to this page. To proceed, please login with an account that has acess</p>
#     {% else %}
#        <p>Please login to se this site</p>
#     {% endif %}
# {% endif %}
#
# <form method="post" actions="{% url 'login' %}">
#    {% csrf_token %}
#    {{ form.as_p }} => form is a context variable like in symfony
#    <input type="submit" class="btn" value="login" />
#    <input type="hidden" name="next" value="{{ next }}" />
# </form>
#
# To access the information of the user in the view we use the variable user
# To access in the controller we use request.user.username
#
# Views that require a logged in user
#
# You cold check user.is_authenticated at the beggining of each view.
#
# The best way of protect view o content.
#
# from django.contrib.auth.mixins import LoginRequiredMixin
#
# class ProtectView(LoginRequiredMixin, View): => Making our class inherence from LoginRequiredMixin we assure our selves that, that view is behind the loggin
#
# FORMS IN DJANGO
#
# forms.py is connected to templates, to models, to views
#
# Handling forms is a copmlex Business. Consider Django's admin, where numerous items of data of several different types may need to be prepared for display in a form
# rendered as HTML, edited using a convenient interface, returned to the server, validated and cleaned up, and the saved or passed on for further proccesing. Django's
# form functionallity can simplify and automate vast portions of this work, and can also do it more securely than most programmers would be able to do in code they
# wrote themselves
#
# Django handles three distinct parts of the work involved in forms:
#     - preparing and restructuring data to make it ready for rendering
#     - creating HTML forms for the data
#     - receiving and processing submitted forms and data from the client
#
# Form Handling Flow is Actually Complex
#
# Create - Produce empty form, check post data for validity, re-display form with erros
#          if necessary, add the data to the database, and redirect the user to a success
#          page with a success message
# Update - Load old data, form with old data, check post data for validity, re-display form
#          with errors if neccesary, update the data to the database, and redirect the user
#          to a success page with a success message
# Delete - Load old data, produce confirmation page with a POST form, receive the post data,
#          delete the record, and redirect the user
#
# Django forms act as "glue"
# Generate the necessary HTML to send to the browser
#    - Allow for consistent look and feel across all the forms in an application
# Receive the POST data coming back from the browser
# Validate the incoming POST data and produce HTML for an error screen if necessary
# Move the data from the form into a model and then store it in the database automatically
#
# forms.py
#
# form django import forms
# form django.core.exceptions import ValidationError
# from django.core import validators
#
# FORM NOT CONNECTED TO A MODEL
# class BasicForm(forms.Form):
#       title = forms.CharField(validators=[
#           validators.MinLengthValidator(2, "Please enter 2 or more characters")
#       ])
#       mileage = forms.IntegerField()
#       purchase_date = froms.DateField()
#
# from form.forms import BasicForm
#
# def example(request): => This creates the entire HTML page with the form as a table
#     form = BasicForm()
#     return HttpResponse(form.as_table())
#
# The best example is to use it in a template
# def example(request): => This creates the entire HTML page with the form as a table
#     form = BasicForm()
#     ctx = {'form' : form}
#     return render(request, 'form/form.html', ctx)
#
# If we have an edit form we pass the data when we create a form
# form = BasicForm(old_data)
#
# {{ form.as_table }}
#
# Models Form
#
# from django.forms import ModelForm
# from auto.models import Make
#
# class MakeForm(ModelForm);
#    class Meta:
#      model = make
#      fields = '__all__'
