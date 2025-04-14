from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equipment ,CategoryEquipment
from .serializers import EquipmentSerializer ,CategoryEquipmentSerializer



class CategoryListAPIView(APIView):
    def get(self, request):
        categories = CategoryEquipment.objects.all()
        serializer = CategoryEquipmentSerializer(categories, many=True)
        return Response(serializer.data)



from rest_framework.generics import ListAPIView

class EquipmentByCategoryAPIView(ListAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        return Equipment.objects.all()


class EquipmentCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.user_type != 'equipment_owner':
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['owner'] = request.user.id

        serializer = EquipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
