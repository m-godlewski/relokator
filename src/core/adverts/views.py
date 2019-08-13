from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Advert
from .forms import AdvertModelForm


def advert_list_view(request):
    qs = Advert.objects.all()
    template_name = 'adverts/adverts.html'
    if request.user.is_authenticated:
        my_qs = Advert.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    context = {'object_list': qs}
    return render(request, template_name, context) 


@login_required
def advert_create_view(request):
    form = AdvertModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = AdvertModelForm()
    template_name = 'adverts/adverts_create.html'
    context = {
        "form":form
    }
    return render(request, template_name, context)