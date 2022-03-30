from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")


def newbooking(request):
    return render(request, "new_booking.html")

def existingbooking(request):
    return render(request, "existing_booking.html")