from django.shortcuts import render

# Create your views here.
from .utils import editor
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404,HttpResponseRedirect,HttpResponse
from django.contrib import messages
import datetime




def file(request):
    if request.method == "POST":

        old=request.POST.getlist('old_value[]')
        new=request.POST.getlist('new_value[]')
        print(old)
        print(new)
        if "" in old:
            return HttpResponse("Values cannot be empty")
        if "" in new:
            return HttpResponse("Values cannot be empty")

        file=request.FILES['pdf_file']
       
        response=editor(file,old,new)
        return response

    return render(request,'file.html')



def custom_404(request, exception):
    return render(request, '404.html', status=404)