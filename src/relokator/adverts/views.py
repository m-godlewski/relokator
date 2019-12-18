import os
from core.settings import BASE_DIR
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Advert
from .forms import AdvertModelForm
from companies.models import Company


# CREATE
@login_required
def advert_create_view(request):
    """ advert creation view
    
    Returns:
        rendering advert creation template

    """

    template_name = "adverts/adverts-create.html"

    # get empty creation form
    form = AdvertModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user  # setting current user as owner of advert
        form.save()
        form = AdvertModelForm()

    # after successfull creation redirect to user adverts page
    if request.method == "POST":
        return redirect(f"/accounts/{request.user}/adverts")

    context = {"form": form}
    return render(request, template_name, context)


# RETRIEVE
def advert_detail_view(request, advert_id:str):
    """ advert detail view
    
    Arguments:
        advert_id {str} -- [id of advert]

    Returns:
        rendering advert detail template

    """

    template_name = "adverts/adverts-detail.html"

    # getting advert by advert_id
    advert = get_object_or_404(Advert, id=advert_id)

    # get comapnies in advert.city
    companies = Company.objects.filter(Q(location=advert.city))

    context = {"advert": advert, "companies": companies}
    return render(request, template_name, context)


def advert_browse_view(request):
    """ adverts browse view
    
    Returns:
        rendering adverts browse template

    """
    
    template_name = "adverts/adverts-browse.html"

    # getting all adverts
    adverts = Advert.objects.all()

    context = {"adverts": adverts}
    return render(request, template_name, context)


# UPDATE
@login_required
def advert_update_view(request, advert_id:str):
    """ advert update view
    
    Arguments:
        advert_id {str} -- [id of advert]

    Returns:
        rendering advert update template

    """

    template_name = "adverts/adverts-update.html"

    # get advert by id
    advert = get_object_or_404(Advert, id=advert_id)

    # fill form with advert data
    form = AdvertModelForm(data=request.POST or None, files=request.FILES, instance=advert)

    if form.is_valid():
        form.save()

    # if current user is not owner of advert, redirect to error page
    if request.user.username != str(advert.user):
        return render(request, "website/error_404.html")

    context = {
        "form": form,
        "title": "Edytujesz ogłoszenie '{}'".format(str(advert.title))
    }
    return render(request, template_name, context)


# DELETE
@login_required
def advert_delete_view(request, advert_id:str):
    """ advert delete view
    
    Arguments:
        advert_id {str} -- [id of advert]

    Returns:
        rendering advert delete template

    """

    template_name = "adverts/adverts-delete.html"

    # get advert by advert_id
    advert = get_object_or_404(Advert, id=advert_id)

    # if current user is not owner of advert, redirect to error page
    if request.user.username != str(advert.user):
        return render(request, "website/error_404.html")

    # if user press delete button, delete advert and redirect
    if request.method == "POST":

        advert.delete()  # object delete
        
        if advert.image:  # if adver has image
            image_path = BASE_DIR + advert.image.url  # image file path
            os.remove(image_path)  # delete file

        return redirect(f"/accounts/{request.user}/adverts")

    context = {"object": advert}
    return render(request, template_name, context)
