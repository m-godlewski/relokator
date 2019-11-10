from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# CREATE
@login_required
def company_create_view(request):
    pass


# RETRIEVE
def company_info_view(request);
    pass


# UPDATE
@login_required
def company_update_view(request):
    pass


# DELETE
@login_required
def company_delete_view(request):
    pass