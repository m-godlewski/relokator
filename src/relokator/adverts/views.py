from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Advert
from .forms import AdvertModelForm
from maps.models import GoogleMapsLocation


# CREATE
@login_required
def advert_create_view(request):
    template_name = "adverts/adverts-create.html"
    form = AdvertModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = AdvertModelForm()

    context = {"form": form}
    return render(request, template_name, context)


# RETRIEVE
def advert_detail_view(request, advert_id):
    template_name = "adverts/adverts-detail.html"
    advert = get_object_or_404(Advert, id=advert_id)
    advert_maps_url = GoogleMapsLocation(advert.address, advert.city)

    context = {
        "title": str(advert.title),
        "advert": advert,
        "advert_maps_url": advert_maps_url.get_location_url(),
    }
    return render(request, template_name, context)


def advert_browse_view(request):
    template_name = "adverts/adverts-browse.html"
    query = Advert.objects.all()

    context = {"title": "Ogłoszenia", "query": query}
    return render(request, template_name, context)


# UPDATE
@login_required
def advert_update_view(request, advert_id):
    template_name = "adverts/adverts-edit.html"
    advert = get_object_or_404(Advert, id=advert_id)
    form = AdvertModelForm(request.POST or None, instance=advert)

    if form.is_valid():
        form.save()

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
    advert = get_object_or_404(Advert, id=advert_id)

    if request.method == "POST":
        advert.delete()
        return redirect(f"/accounts/{request.user}/adverts")

    context = {"object": advert}
    return render(request, template_name, context)
