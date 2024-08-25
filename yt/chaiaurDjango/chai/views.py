from django.shortcuts import render
from . import models
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
# Create your views here.


def all_chai(request):
    chais = models.ChaiVariety.objects.all()
    return render(request, "chai/allChai.html", {'chais':chais})


def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,"chai/chaiDetail.html",{'chai':chai})
