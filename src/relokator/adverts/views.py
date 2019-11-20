from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Advert
from .forms import AdvertModelForm
from companies.models import Company


# CREATE
@login_required
def advert_create_view(request):
    template_name = "adverts/adverts-create.html"
    
    # get empty creation form
    form = AdvertModelForm(request.POST or None, request.FILES or None) 

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user # setting current user as owner of advert
        form.save()
        form = AdvertModelForm()

    context = {"form": form}
    return render(request, template_name, context)


# RETRIEVE
def advert_detail_view(request, advert_id):
    template_name = "adverts/adverts-detail.html"

    # getting advert by advert_id
    advert = get_object_or_404(Advert, id=advert_id)

    # get comapnies in advert.city
    companies = Company.objects.filter(Q(location=advert.city)) 

    context = {
        "title": advert.title,
        "advert": advert,
        "advert_maps_url": advert.map_url,
        "companies": companies
    }
    return render(request, template_name, context)


def advert_browse_view(request):
    template_name = "adverts/adverts-browse.html"

    # get all adverts
    adverts = Advert.objects.all()

    context = {"title": "Ogłoszenia", "adverts": adverts}
    return render(request, template_name, context)


# UPDATE
@login_required
def advert_update_view(request, advert_id):
    template_name = "adverts/adverts-edit.html"

    # get advert by id
    advert = get_object_or_404(Advert, id=advert_id)

    # fill form with advert data
    form = AdvertModelForm(request.POST or None, instance=advert)

    if form.is_valid():
        form.save()

    # if current user is not owner of advert, redirect to error page
    if request.user.username != str(advert.user):
        return render(request, "website/error_404.html")

    context = {
        "form": form,
        "title": "Edytujesz ogłoszenie '{}'".format(str(advert.title)),
    }
    return render(request, template_name, context)


# DELETE
@login_required
def advert_delete_view(request, advert_id):
    template_name = "adverts/adverts-delete.html"

    # get advert by advert_id
    advert = get_object_or_404(Advert, id=advert_id)

    # if current user is not owner of advert, redirect to error page
    if request.user.username != str(advert.user):
        return render(request, "website/error_404.html")

    # if user press delete button, delete advert and redirect
    if request.method == "POST":
        advert.delete()
        return redirect(f"/accounts/{request.user}/adverts")

    context = {"object": advert}
    return render(request, template_name, context)