from django.shortcuts import render,HttpResponseRedirect
from .forms import calForm

# Create your views here.
def cal(request):
    c=" "
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2    
    except:
        c="invalid operation"
    print(c)
    return render(request,"calculation/calculate.html",{'c':c})        
