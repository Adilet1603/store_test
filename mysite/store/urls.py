from venv import create
from xml.etree.ElementInclude import include

from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()


router.register('category', CategoryViewSet, basename='category')
router.register('user', UserProfileViewSet, basename='user')
router.register('ImageProduct', ImageProductViewSet, basename='ImageProduct')
router.register('order', OrderViewSet, basename='Order')
router.register('orderitem', OrderItemViewSet, basename='orderitem')


urlpatterns = [
     path ('', include(router.urls)),
     path ('product/', ProductViewSet.as_view(), name = 'product'),
     path ('product/<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve'}), name = 'product_detail'),

     path ('review/', ReviewProductViewSet.as_view({'get': 'list'}), name = 'review-list'),
     path ('review/<int:pk>/', ReviewProductViewSet.as_view({'get': 'retrieve'}), name = 'review-detail'),

     path ('rating/', RatingViewSet.as_view({'get': 'list'}), name = 'rating-list' ),
     path ('rating/<int:pk>/', RatingDetailViewSet.as_view({'get': 'list'}), name = 'rating-detail'),

     path ('favorite_item/', FavoriteItemViewSet.as_view({'get': 'list'}), name = 'favorite_item-list'),
     path ('favorite/', FavoriteViewSet.as_view({'get': 'list'}), name = 'favorite-list'),
     path ('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'list'}), name = 'favorite-list'),

     path('accounts/', include('allauth.urls')),

     path('cart/', CartViewSet.as_view({'get': 'list'}), name='cart-list'),
     path('cart_item/', CartItemViewSet.as_view({'get': 'list'}), name='cart_item-list'),
     path('cart_item/<int:pk>/', CartItemViewSet.as_view({'get': 'list'}), name='cart_item-list'),
]






