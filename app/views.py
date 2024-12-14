from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def redirect_to_admin(request):
    return redirect('adminpannel')#Redirect authenticated users to the admin page

def adminpannel(request):
    return render(request,'app.html')
  