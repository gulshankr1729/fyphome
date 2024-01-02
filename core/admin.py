from django.contrib import admin
from core.models import Residence, Category, Vendor, wishlist, ResidenceImages, ResidenceReviews, Address

class ResidenceImagesAdmin(admin.TabularInline):
    model = ResidenceImages

class ResidenceAdmin(admin.ModelAdmin):
    inlines = [ResidenceImagesAdmin]
    list_display = ['user', 'title', 'Residence_image', 'price','category','vendor', 'featured', 'Residence_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class ResidenceReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'Residence', 'review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'Residence', 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']

admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ResidenceReviews, ResidenceReviewsAdmin)
admin.site.register(wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
