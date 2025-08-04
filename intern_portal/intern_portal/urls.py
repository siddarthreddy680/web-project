from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('api/intern/', views.api_intern, name='api_intern'),
    path('api/leaderboard/', views.api_leaderboard, name='api_leaderboard'),
]
