from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImagesProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = '__all__'





class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    image_product= ImagesProductSerializers(read_only=True, many=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductSimpleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_image']


class ReviewProductSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()

    class Meta:
        model = ReviewProduct
        fields = ['id', 'user', 'comment', 'created_at']

class RatingSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    product = ProductSimpleSerializers()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'product', 'stars']

class RatingDetailSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    product = ProductSimpleSerializers()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'product', 'stars']

class ProductDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    image_product= ImagesProductSerializers(read_only=True, many=True)
    review_product = ReviewProductSerializers(read_only=True, many=True)
    rating_product = RatingSerializers(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'product_image', 'image_product', 'product_name',
                  'description', 'price', 'product_video', 'review_product', 'rating_product']





class FavoriteItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class FavoriteDetailSerializers(serializers.ModelSerializer):

        user = UserProfileSerializers()
        favorite_items= FavoriteItemSerializers(read_only=True, many=True)
        class Meta:
             model = Favorite
             fields = ['id', 'user', 'favorite_items']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'




class CartItemSerializers(serializers.ModelSerializer):



    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    items = CartItemSerializers(read_only=True, many=True )
    class Meta:
        model = Cart
        fields = ['id','user', 'items']
