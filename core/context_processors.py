from core.models import Residence, Category, Vendor, wishlist, ResidenceImages, ResidenceReviews, Address

    


def default(request):
    categories = Category.objects.all()
    return {
        'categories':categories,
    }
