from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')
def team(request):
    return render(request,'team.html')
def registration(request):
    return render(request,'registration.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')

