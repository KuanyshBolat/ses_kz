from django.shortcuts import render


# Create your views here.
def lk(request):
    return render(template_name='lk.html', request=request)
