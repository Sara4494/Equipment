from rest_framework.views import APIView
from rest_framework.response import Response
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
