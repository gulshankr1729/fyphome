from django.shortcuts import render, HttpResponse, get_list_or_404
from core.models import Residence, Category, Vendor, wishlist, ResidenceImages, ResidenceReviews, Address
from django.contrib.auth.decorators import login_required

def index(request):
    Residences = Residence.objects.filter(Residence_status="published", featured=True).order_by("-id")
    total_residences = Residence.objects.count()

    context = {
        "Residences":Residences,
        "total_residences": total_residences,
    }
    return render(request, 'core/index.html',context)


def residence_view(request):
    Residences = Residence.objects.filter(Residence_status="published").order_by("-id")
    categories = Category.objects.all()
    # tags = Tag.objects.all().order_by("-id")[:6]

    context = {
        "Residences":Residences,
        "categories":categories,
        # "tags":tags,
    }
    return render(request, 'core/residence.html', context)



@login_required(login_url='../sign-in/')
def search_view(request):
    query = request.GET.get("q")

    Residences = Residence.objects.filter(description__icontains=query).order_by("-date")

    context = {
        "Residences": Residences,
        "query": query,
    }
    return render(request, 'core/search.html', context)


def residence_detail_view(request, Rid):
    residence = Residence.objects.get(Rid=Rid)
    R_image = residence.R_images.all()

    context = {
        "R": residence,
        "R_image": R_image,
    }

    return render(request, "core/residence_detail.html", context)


@login_required
def my_listings_view(request):
    # Filter residences based on the logged-in user
    residence = Residence.objects.filter(user=request.user)
    return render(request, 'core/my_listing.html')

def filter_residence(request):
    Categories = request.GET.getlist("category[]")

    residence = Residence.objects.filter(Residence_status="published").order_by("-id").distinct(
        
    )