# DjangoProject
This Is For Rest Framework Project. Create Real Time Application


Class-based views
A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views.
All views inherit from the View class, which handles linking the view in to the URLs, HTTP method dispatching and other simple features. 
RedirectView is for a simple HTTP redirect, and TemplateView extends the base class to make it also render a template.
Introduction to class-based views
Class-based views provide an alternative way to implement views as Python objects instead of functions. 
They do not replace function-based views, but have certain differences and advantages when compared to function-based views:
•	Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
•	Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.




Steps to Create a class based view
•	To create a class-based view, start by creating a class that inherits from django.views.generic.View or one of its subclasses.
•	In your path, specify the view method as the name of the new class, plus .as_view().
Example:
path('', Sample.as_view()),
path('open/', Sample.as_view()),
•	In your class, write a get method that takes as arguments self (as always), request (the HttpRequest), and any other arguments from the request as specified in your URLconf.
•	In your get method, use the same logic you'd have used in an old view, except that you can assume the request method is GET. Return an HttpResponse as usual.
•	If you need to handle POST, write a post method, just like your get method except that you can assume the request method is POST.
•	Any request method that you don't write a handler method for will automatically get back a "method not allowed" response; you don't have to do anything special.




Example
from django.http import HttpResponse
from django.views import View
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
# urls.py
from django.urls import path
from myapp.views import MyView
urlpatterns = [
    path('about/', MyView.as_view()),
]
Built-in class-based views
•	Base views
o	View
o	TemplateView
o	RedirectView
•	Generic display views
o	DetailView
o	ListView
