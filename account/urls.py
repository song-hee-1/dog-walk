from django.urls import path
from django.urls import include


urlpatterns = [
    path('account/', include('dj_rest_auth.urls')),
    path('account/', include('dj_rest_auth.registration.urls')),

]
