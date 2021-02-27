from django.urls import path
from pages.views import home, menu,about, timing, contact,add

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('menu/',menu.as_view(),name="menu"),
    path('about/',about.as_view(),name="about"),
    path('timing/',timing.as_view(),name="timing"),
    path('contact/',add.as_view(),name="page.add"),
]
