from django.contrib import admin
from .models  import *


class ImagesProductInline(admin.TabularInline):
    model = ImagesProduct
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesProductInline]

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewProduct)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)