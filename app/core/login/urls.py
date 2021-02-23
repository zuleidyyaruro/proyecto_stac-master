from django.urls import path

from core.login.views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
    #path('login2', LoginFormView2.as_view(), name='login2'),

]