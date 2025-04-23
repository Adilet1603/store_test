from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from .pagination import ProductPagination

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['price']
    filterset_class = ProductFilter
    pagination_class = ProductPagination

class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializers


class ReviewProductViewSet(viewsets.ModelViewSet):
    queryset = ReviewProduct.objects.all()
    serializer_class = ReviewProductSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers





class RatingDetailViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingDetailSerializers

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteItemSerializers

class FavoriteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteItemSerializers


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializers


class CartViewSet(generics.ListAPIView):
    serializer_class = CartSerializers

    def get_queryset(self):
        return Cart.objects.filter(user= self.request.user)

class CartItemViewSet(generics.ListAPIView):
    serializer_class = CartItemSerializers

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(self.request.user)
        serializer.save(cart=cart)

# class CartItemDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializers