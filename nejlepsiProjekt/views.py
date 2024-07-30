from django.shortcuts import render, redirect
from .models import Partner, Review
from .forms import PartnerForm, ReviewForm, UserRegisterForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def partner_list(request):
    partners = Partner.objects.all()
    review_form = ReviewForm()
    return render(request, 'partner_list.html', {'partners': partners, 'review_form': review_form})

def rate_partner(request, partner_id):
    partner = Partner.objects.get(id=partner_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.partner = partner
            review.customer = request.user  # Assuming the user is logged in
            review.save()
            return redirect('partner_list')
    else:
        form = ReviewForm()
    return render(request, 'rate_partner.html', {'form': form, 'partner': partner})


def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'add_partner.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})