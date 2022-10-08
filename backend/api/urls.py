from django.urls import path
from api.views import VesselApiView, VesselDetailApiView

urlpatterns = [
    path('vessel/', VesselApiView.as_view()),
    path('vessel/<str:name>/', VesselDetailApiView.as_view()),
]
