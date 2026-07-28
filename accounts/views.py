from django.shortcuts import render
from django.http import HttpResponse
from .models import Enquiry

# Create your views here.


def Home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == "POST":

            Enquiry.objects.create(
            full_name=request.POST.get('full_name'),
            gender=request.POST.get('gender'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            city=request.POST.get('city'),
            current_class=request.POST.get('class'),
            school=request.POST.get('school'),
            course=request.POST.get('course'),
            batch=request.POST.get('batch'),
            mode=request.POST.get('mode'),
            message=request.POST.get('message'),
        )

            return render(request, 'contact-form.html', {
                'success': 'Your enquiry has been submitted successfully!'
        })
    return render(request, 'contact-form.html')


def about(request):
    return HttpResponse('This is about page')
    return render(request,'contact-form.html')


def about(request):
    return HttpResponse('This is about page')


def admin_dashboard(request):
    enquiries = Enquiry.objects.all()

    return render(request, "admin-dashboard.html", {
        "enquiries": enquiries
    })