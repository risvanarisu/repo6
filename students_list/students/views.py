from django.shortcuts import render

# Create your views here.
def registerattendance(request):
    return render(request,"attendance/present.html")