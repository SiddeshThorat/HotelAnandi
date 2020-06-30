from django.urls import path
from . import views

urlpatterns = [
       path("",views.index,name="index"),
       path("home",views.index,name="index"),
       path("order",views.order,name="order"),
       path("contact",views.contact,name="contact"),
       path("team",views.team,name="team"),
       path("about",views.about,name="about"),
       path("review",views.review,name="review"),
       path("menu",views.menu,name="menu"),       
       

]