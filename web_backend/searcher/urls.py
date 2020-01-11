from django.urls import path

from .views import *


urlpatterns = [
    path('test', hello),
    path('registration', registration),
    path('authentication', authentication),

]
