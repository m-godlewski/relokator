from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Company
from .forms import CompanyModelForm
from accounts.models import Account


# CREATE
@login_required
def company_create_view(request):
    """ company creation view
    
    Returns:
        rendering company registration template

    """

    template_name = "companies/companies-create.html"

    # getting empty creation form
    form = CompanyModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user # setting current user as owner of company
        form.save()
        form = CompanyModelForm()

    # after success creation redirect to account companies view
    if request.method == "POST":
        return redirect(f"/accounts/{request.user}/companies")

    context = {"title": "Rejestracja firmy", "form": form}
    return render(request, template_name, context)


# RETRIEVE
def company_detail_view(request, company_id:str):
    """ company detail view

    Arguments:
        company_id {str} -- [id of company]
    
    Returns:
        rendering company detail template with company data

    """

    template_name = "companies/companies-info.html"

    # getting company by company_id
    company = get_object_or_404(Company, id=company_id)

    # getting contact to company owner
    owner = Account.objects.get(username=str(company.user))

    context = {
        "title": company.name,
        "company": company,
        "phone_number": owner.phone_number,
        "email": owner.email
    }
    return render(request, template_name, context)


def company_browse_view(request):
    """ companies browsing view

    Returns:
        rendering companies browsing view

    """

    template_name = "companies/companies-browse.html"

    # get all companies
    companies = Company.objects.all()

    context = {"title": "Firmy przeprowadzkowe", "companies": companies}
    return render(request, template_name, context)


# UPDATE
@login_required
def company_update_view(request, company_id:str):
    """ company update view

    Arguments:
        company_id {str} -- [id of company]
    
    Returns:
        rendering company update template with company data in form

    """
    template_name = "companies/companies-update.html"

    # get company by company_id
    company = get_object_or_404(Company, id=company_id)

    # fill form with company data
    form = CompanyModelForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()

    # if current user is not owner of company, redirect to error page
    if request.user.username != str(company.user):
        return render(request, "website/error_404.html")

    # after successfull update redirect to account companies view
    if request.method == "POST":
        return redirect(f"/accounts/{request.user}/companies")

    context = {"title": "Edytycja firmy '{}'".format(str(company.name)), "form": form}
    return render(request, template_name, context)


# DELETE
@login_required
def company_delete_view(request, company_id:str):
    """ company delete view

    Arguments:
        company_id {str} -- [id of company]
    
    Returns:
        rendering company delete template

    """
    # TODO
    pass
