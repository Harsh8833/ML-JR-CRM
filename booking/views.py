from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import newBooking

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

def saveEnquiry(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        phone=request.POST.get('phone')
        form=request.FILES.get('form')
        pan=request.FILES.get('pan')
        aadhar=request.FILES.get('aadhar')

        en=newBooking(cname=cname, phone=phone, form=form, pan=pan, aadhar=aadhar)
        en.save()
    return render(request,"new_booking.html")