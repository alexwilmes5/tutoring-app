from django.urls import path 

from .views import HomePageView, TAProfileView 

urlpatterns = [ 
path("", HomePageView.as_view(), name="home"),
path("tas/<str:name>/", TAProfileView.as_view(), name="ta_detail"),
]