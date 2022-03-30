from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def newbooking(request):
    return render(request, 'new_booking.html')


@login_required
def existingbooking(request):
    return render(request, 'existing_booking.html')