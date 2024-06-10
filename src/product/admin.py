from django.contrib import admin
from product.models import Variant, ProductImage, Product, ProductVariantPrice, ProductVariant

admin.site.register(Variant)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
admin.site.register(ProductImage)