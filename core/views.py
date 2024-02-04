from django.shortcuts import render, get_list_or_404
from core.models import Residence, Category, Vendor, ResidenceImages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from userauths.models import User

def index(request):
    Residences = Residence.objects.filter(Residence_status="published", featured=True).order_by("-id")
    total_residences = Residence.objects.count()
    user_count = User.objects.count()

    context = {
        "Residences":Residences,
        "total_residences": total_residences,
        'active_page': 'index',
        'user_count': user_count,

    }
    return render(request, 'core/index.html',context=context)


def residence_view(request):
    Residences = Residence.objects.filter(Residence_status="published").order_by("-id")
    categories = Category.objects.all()

    context = {
        "Residences":Residences,
        "categories":categories,
        'active_page': 'residence',
    
    }
    return render(request, 'core/residence.html', context = context)




def search_view(request):
    query = request.GET.get("q")

    Residences = Residence.objects.filter(address__icontains=query).order_by("-date")

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



def my_listings_view(request):
    # Filter residences based on the logged-in user
    residence = Residence.objects.filter(user=request.user)
    
    context = {
        "residence": residence,
        'active_page': 'my_listing',
    }
    return render(request, 'core/my_listing.html', context=context)

def filter_residence(request):
    Categories = request.GET.getlist('Category[]')
    minimum = request.GET.get('minimum')
    maximum = request.GET.get('maximum')

    residences = Residence.objects.filter(Residence_status="published").order_by("-id").distinct()

    if(minimum):
        residences = residences.filter(price__gt=minimum).distinct()
    if(maximum):
        residences = residences.filter(price__lt=maximum).distinct()
    if len(Categories) > 0:
        residences = residences.filter(category__id__in=Categories).distinct()

    
    data = render_to_string("core/async/residence.html", {"Residences": residences})
    return JsonResponse({"data": data})
    

def profile_view(request):
    return render(request, 'core/profile.html')
