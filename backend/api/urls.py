from django.urls import path
from api.views import VesselApiView, VesselDetailApiView

urlpatterns = [
    path('vessel/', VesselApiView.as_view()),
    path('vessel/<int:id>/', VesselDetailApiView.as_view()),
]
