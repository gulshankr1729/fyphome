from django import views
from django.urls import path
from core.views import index, residence_view, search_view, residence_detail_view, my_listings_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("residences/", residence_view, name="residence"),
    path("my_listing/", my_listings_view, name="my_listing"),
    path("residence/<str:Rid>", residence_detail_view, name="residence_detail"),

    # search
    path("search/", search_view, name="search"),
]

