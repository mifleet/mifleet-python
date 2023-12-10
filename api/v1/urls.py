from django.urls import include, path

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('expenses/', include('expenses.urls')),
    path('teachers/', include('teachers.urls')),
    path('vehicles/', include('vehicles.urls')),
]
