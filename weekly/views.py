from django.shortcuts import render
from .models import WeeklyCharProgress


def index(request):
    weekly_char_progresses = WeeklyCharProgress.objects.all()
    context = {"weekly_char_progresses": weekly_char_progresses}
    return render(request, "weekly/index.html", context)
