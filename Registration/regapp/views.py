from django.shortcuts import render

# Create your views here.
from regapp.forms import StudentForm
from django.shortcuts import redirect

def form_view(request):
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('/')
    return render(request,'star/Home.html',{'form':form})        
