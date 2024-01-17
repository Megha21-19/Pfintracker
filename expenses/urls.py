#expenses/urls.py

from django.urls import path
from . import views
from .views import SignUpView, CustomLoginView, root_view, user_dashboard_view,reports_view,contactus_view,graphics_view

urlpatterns = [
    path('', root_view, name='root'),
    path('signup_login/', SignUpView.as_view(), name='signup_login'),
    path('login/', CustomLoginView.as_view(), name='login'),
      path('logout/', CustomLoginView.as_view(), name='logout'),
     path('dashboard/', user_dashboard_view, name='user_dashboard'),
     path('dashboard/reports/',reports_view,name='reports'),
     path('dashboard/contact_us/',contactus_view,name='contact_us'),
     path('dashboard/graphics',graphics_view,name='graphics')
    # Add other paths as needed,
]
