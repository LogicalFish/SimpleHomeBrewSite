
from django.urls import path
from . import views

urlpatterns = [
    path('<int:dietype>/', views.dice, name='dice'),

]
