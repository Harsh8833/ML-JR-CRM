from django.shortcuts import render

# Create your views here.
def newbooking(request):
    return render(request, 'new_booking.html')

def existingbooking(request):
    return render(request, 'existing_booking.html')