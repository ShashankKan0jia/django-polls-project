# polls/urls.py

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('owner', views.owner, name='owner'), # Stays the same
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # Changed to pk
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # Changed to pk
    path('<int:question_id>/vote/', views.vote, name='vote'), # Stays the same
]