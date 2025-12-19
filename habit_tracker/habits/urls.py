from django.urls import path
from .views import (
    HabitListCreateAPIView,
    HabitCompleteAPIView,
    HabitStatsAPIView,
)

urlpatterns = [
    path('', HabitListCreateAPIView.as_view()),         
    path('<int:habit_id>/log/', HabitCompleteAPIView.as_view()),  
    path('stats/', HabitStatsAPIView.as_view()),         
]
