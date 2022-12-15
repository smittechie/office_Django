from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # data ={
    #     'title':"Home page",
    #     'bdata':"MY name is  smit  ",
    #     'clist':['javascript','react','DSA'],
    #     'student_details':[
    #         {'name':'pradeep','phone':9999999999},
    #         {'name':'jaydeep','phone':8888888888}
    #     ]
    # }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def course(request):
    return HttpResponse("welcome to my course")

def coursedetail(request,courseid):
    return HttpResponse(courseid)