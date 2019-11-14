from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Company
from .forms import CompanyModelForm


# CREATE
@login_required
def company_create_view(request):
    template_name = "companies/companies-create.html"
    form = CompanyModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = CompanyModelForm()

    context = {
        "title": "Rejestracja firmy",
        "form" : form
    }
    return render(request, template_name, context)


# RETRIEVE
def company_detail_view(request, company_id):
    template_name = "companies/companies-info.html"
    context = {}
    return render(request, template_name, context)


def company_browse_view(request):
    template_name = "companies/companies-browse.html"
    query = Company.objects.all()

    context = {
        "title": "Firmy przeprowadzkowe",
        "query": query
    }
    return render(request, template_name, context)


# UPDATE
@login_required
def company_update_view(request):
    pass


# DELETE
@login_required
def company_delete_view(request):
    pass