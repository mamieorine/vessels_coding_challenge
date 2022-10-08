from django.urls import path
from api.views import VesselApiView

urlpatterns = [
    path('vessel/', VesselApiView.as_view()),
]
