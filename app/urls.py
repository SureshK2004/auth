# Create your views here.
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import redirect_to_admin

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('redirect-to-admin/', redirect_to_admin, name='redirect_to_admin'),
]


from django.contrib.auth.views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
