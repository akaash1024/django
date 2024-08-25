
from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.all_chai, name="allchai"),
    path("<int:chai_id>/", views.chai_details, name="ChaiDetails"),
]
