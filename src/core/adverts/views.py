from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AdvertModelForm

@login_required
def advert_create_view(request):
    form = AdvertModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = AdvertModelForm()
    template_name = 'adverts/adverts-create.html'
    context = {
        "form":form
    }
    return render(request, template_name, context)