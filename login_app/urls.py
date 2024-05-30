
from django.urls import path,include
from  login_app.views import sgin_up,sgin_in,forget,otp,password

urlpatterns = [
  
    path('reg',sgin_up),
     path('log',sgin_in),
     path('forget',forget),
     path('otp',otp),
     path('passwords',password),
]


