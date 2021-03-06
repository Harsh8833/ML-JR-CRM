from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from booking.models import newBooking
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def otpauth(request):
    return render(request, 'otp_auth.html')

@login_required
def newbooking(request):
    return render(request, 'new_booking.html')

@login_required
def search(request):
    if request.method=="POST":
        bid=request.POST['bid']
        customer= newBooking.objects.filter(booking_id=bid)
        if (len(customer) > 0):
            return render(request, 'ledger_menu.html', {'bid':bid, 'customer':customer[0]})
        else:
            return render(request, 'invalid_booking.html')
    else:
        return render(request, 'invalid_booking.html')

@login_required
def existingbooking(request):
    return render(request, 'existing_booking.html')


@login_required
def saveEnquiry(request):
    try:
        if request.method=="POST":
            cname=request.POST.get('cname')
            phone=request.POST.get('phone')
            form=request.FILES.get('form')
            pan=request.FILES.get('pan')
            aadhar=request.FILES.get('aadhar')

            en=newBooking(cname=cname, phone=phone, form=form, pan=pan, aadhar=aadhar)
            en.save()
            messages.success(request, "Customer added successfully")
    except:
        messages.error(request, "Unable to add Customer")
        
    return render(request,"new_booking.html")