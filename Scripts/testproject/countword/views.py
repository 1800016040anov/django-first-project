from django.shortcuts import render,redirect
from django.http import HttpResponse


def input(request):
    
     return render(request, 'index.html')
def output(request):
    val1 = request.GET['input1']
    val2 = request.GET['input2']
    request.GET['but']
    jml=""
    for i2 in val2:
        if i2 in val1:
            jml += i2
        
    a = len(jml)
    b= len(val1)
    k = a/b*100
    data ='karakter yang muncul adalah ',a,'/',b, ' dengan presentase : ',k,'%'
    return HttpResponse(data)






   
