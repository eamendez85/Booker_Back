
from rest_framework import viewsets
from rest_framework import generics
from api.serializers.csv_serializers import CsvSerializer
from rest_framework.response import Response

class CsvCreateApiView(generics.CreateAPIView):
    serializer_class = CsvSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        
        return Response(serializer.data)