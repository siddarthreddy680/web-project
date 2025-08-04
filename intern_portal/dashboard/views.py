from django.http import JsonResponse
from django.shortcuts import render

# Dummy intern data
intern_data = {
    "name": "Jane Doe",
    "referral_code": "janedoe2025",
    "donations": 1750,
    "rewards": [
        {"title": "Bronze Badge", "unlocked": True},
        {"title": "Silver Badge", "unlocked": False},
        {"title": "T-shirt", "unlocked": False}
    ]
}

leaderboard_data = [
    {"name": "Jane Doe", "donations": 1750},
    {"name": "Alex Smith", "donations": 1250},
    {"name": "Sam Lee", "donations": 900},
]


def login_view(request):
    return render(request, "dashboard/login.html")


def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")


def leaderboard_view(request):
    return render(request, "dashboard/leaderboard.html")


def api_intern(request):
    return JsonResponse(intern_data)


def api_leaderboard(request):
    return JsonResponse(leaderboard_data, safe=False)
