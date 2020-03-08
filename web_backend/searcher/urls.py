from django.urls import path

from .views import *


urlpatterns = [
    path('test', hello),
    path('search', search),
    path('doc', get_doc),
    path('registration', registration),
    path('authentication', authentication),

]
