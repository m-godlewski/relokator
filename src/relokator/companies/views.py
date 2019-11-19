from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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

    context = {"title": "Rejestracja firmy", "form": form}
    return render(request, template_name, context)


# RETRIEVE
def company_detail_view(request, company_id):
    template_name = "companies/companies-info.html"
    company = get_object_or_404(Company, id=company_id)

    context = {"title": company.name, "company": company}
    return render(request, template_name, context)


def company_browse_view(request):
    template_name = "companies/companies-browse.html"
    query = Company.objects.all()

    context = {"title": "Firmy przeprowadzkowe", "query": query}
    return render(request, template_name, context)


# UPDATE
@login_required
def company_update_view(request, company_id):
    template_name = "companies/companies-update.html"
    company = get_object_or_404(Company, id=company_id)
    form = CompanyModelForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()

    if request.user.username != str(company.user):
        return render(request, "website/error_404.html")

    context = {"title": "Edytycja firmy '{}'".format(str(company.name)), "form": form}
    return render(request, template_name, context)


# DELETE
@login_required
def company_delete_view(request):
    pass
