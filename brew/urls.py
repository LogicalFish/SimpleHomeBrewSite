
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:job_id>', views.job, name='job'),
    path('<int:job_id>/<int:brew_id>', views.detail, name='brew'),

]
