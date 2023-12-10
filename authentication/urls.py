from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('session/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token)
]