from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vessel
from .serializers import VesselSerializer


class VesselDetailApiView(APIView):
    def put(self, request, id, *args, **kwargs):
        vessel = Vessel.objects.get(id=id)
        serializer = VesselSerializer(
            data=request.data, instance=vessel, many=False)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

        instance = self.get_object(id)
        if not instance:
            return Response(
                {"res": "Object with vessel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            vessel = Vessel.objects.get(id=id)
        except Vessel.DoesNotExist:
            return Response(
                {"res": "Object with vessel does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        vessel.delete()
        return Response({"res": "Vessel deleted!"}, status=status.HTTP_200_OK)


class VesselApiView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = VesselSerializer(Vessel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        vesselDetail = {
            'name': request.data.get('name'),
            'lat': request.data.get('lat'),
            'lng': request.data.get('lng'),
            'address': request.data.get('address')
        }
        serializer = VesselSerializer(data=vesselDetail)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
