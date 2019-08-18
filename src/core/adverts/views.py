from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Advert
from .forms import AdvertModelForm


def advert_detail_view(request, advert_id):
    template_name = 'adverts/adverts-detail.html'
    qs = Advert.objects.filter(Q(id=advert_id))
    qs = qs[0]
    context = {
        'title':str(qs.title),
        'advert': qs
    }
    return render(request, template_name, context) 


@login_required
def advert_create_view(request):
    form = AdvertModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = AdvertModelForm()
    template_name = 'adverts/adverts-create.html'
    context = {"form" : form}
    return render(request, template_name, context)


@login_required
def advert_edit_view(request, advert_id):
    obj = get_object_or_404(Advert, id=advert_id)
    form = AdvertModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'adverts/advert-edit.html'
    context = {
        "form":form,
        "title":'Edytujesz ogłoszenie {}'.format(str(obj.title))
    }
    return render(request, template_name, context)

@login_required
def advert_delete_view(request, advert_id):
    pass