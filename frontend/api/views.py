from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Product, Order, UserProfile
from .serializers import ProductSerializer, OrderSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def place_order(self, request, pk=None):
        product = self.get_object()
        user = request.user
        quantity = request.data.get('quantity', 1)
        total_price = product.price * quantity
        order = Order.objects.create(user=user, product=product, quantity=quantity, total_price=total_price, status='pending')
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_user_profile(self, request, pk=None):
        user_profile = self.get_object()
        return Response(UserProfileSerializer(user_profile).data)
