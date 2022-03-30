from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")


def newBooking(request):
    return render(request, "new_booking.html")

def existingBooking(request):
    return render(request, "existing_booking.html")