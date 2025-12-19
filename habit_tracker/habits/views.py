from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from .models import Habit, HabitLog
from .serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitCompleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id, user=request.user)
        today = timezone.now().date()

        if HabitLog.objects.filter(habit=habit, date_completed=today).exists():
            return Response(
                {"detail": "Habit already completed today"},
                status=status.HTTP_400_BAD_REQUEST
            )

        HabitLog.objects.create(habit=habit, date_completed=today)

        yesterday = today - timedelta(days=1)
        if HabitLog.objects.filter(habit=habit, date_completed=yesterday).exists():
            habit.current_streak += 1
        else:
            habit.current_streak = 1

        habit.longest_streak = max(habit.longest_streak, habit.current_streak)
        habit.save()

        return Response(
            {
                "message": "Habit marked as completed",
                "current_streak": habit.current_streak,
                "longest_streak": habit.longest_streak
            }
        )
class HabitStatsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()

        total_habits = Habit.objects.filter(user=user).count()

        completed_today = HabitLog.objects.filter(
            habit__user=user,
            date_completed=today
        ).count()

        longest_streak = (
            Habit.objects.filter(user=user)
            .order_by('-longest_streak')
            .values_list('longest_streak', flat=True)
            .first() or 0
        )

        return Response({
            "total_habits": total_habits,
            "completed_today": completed_today,
            "longest_streak": longest_streak
        })
