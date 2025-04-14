from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from user.models import CustomUser
from equipment.models import Equipment
from Construction.models import Construction

class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        item_type = request.data.get('item_type')  # 'worker' / 'equipment' / 'construction'
        item_id = request.data.get('item_id')

        if item_type == 'worker':
            item = CustomUser.objects.filter(id=item_id, user_type='worker').first()
        elif item_type == 'equipment':
            item = Equipment.objects.filter(id=item_id).first()
        elif item_type == 'construction':
            item = Construction.objects.filter(id=item_id).first()
        else:
            return Response({'error': 'نوع الطلب غير معروف'}, status=400)

        if not item:
            return Response({'error': 'العنصر غير موجود'}, status=404)

        seller = item.owner if item_type != 'worker' else item
        category = item.category.name if hasattr(item, 'category') else item.get_worker_specialization_display()
        image = item.image if hasattr(item, 'image') else item.profile_image
        price = item.price

        order = Order.objects.create(
            buyer=request.user,
            seller=seller,
            item_type=item_type,
            item_id=item_id,
            category=category,
            image=image,
            price=price
        )

        return Response({'message': 'تم إرسال الطلب بنجاح 🎉'}, status=201)



class MyPurchasesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(buyer=request.user)
        data = OrderSerializer(orders, many=True).data
        return Response(data)

class IncomingOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(seller=request.user)
        data = OrderSerializer(orders, many=True).data
        return Response(data)
