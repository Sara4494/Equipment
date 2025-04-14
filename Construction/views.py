from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Construction ,CategoryConstruction
from .serializers import ConstructionSerializer ,CategoryConstructionSerializer 



class CategoryListAPIView(APIView):
    def get(self, request):
        categories = CategoryConstruction.objects.all()
        serializer = CategoryConstructionSerializer(categories, many=True)
        return Response(serializer.data)
    


from rest_framework.generics import ListAPIView

class ConstructionListAPIView(ListAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer


class ConstructionCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.user_type != 'construction_owner':
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['owner'] = request.user.id

        serializer = ConstructionSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
