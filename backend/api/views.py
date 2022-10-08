from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vessel
from .serializers import VesselSerializer


class VesselApiView(APIView):
    def get(self, request, *args, **kwargs):

        if (Vessel.DoesNotExist):
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = VesselSerializer(Vessel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        vesselDetail = {
            'name': request.data.get('name')
        }
        serializer = VesselSerializer(data=vesselDetail)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
