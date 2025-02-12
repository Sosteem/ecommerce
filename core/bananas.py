# from django.urls import path
# from core.views import index

# app_name="bananas"
# urlpatherns=[
#     path("bananas/",index)
# ]
from django.urls import path
from . import views  # Ensure the correct import

urlpatterns = [
    path("", views.index, name="index"),
]
