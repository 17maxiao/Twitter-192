"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from splash.views import splash
# from login.views import login
# from home.views import home
# from hashtag.views import hashtag
# from profilepage.views import profilepage
from main.views import splash_view, login_view, home_view, profile_view, signup, login_account, logout_view, delete_view, like_view #,hashtag_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash_view, name='splash_view'),
    path('login/', login_view, name='login_view'),
    path('home', home_view, name='home_view'),
    #path('hashtag/', , name='hashtag_view'),
    path('profile/', profile_view, name='profile_view'),
    path('signup', signup, name='signup'),
    path('signin', login_account, name='login_account'),
    path('logout', logout_view, name='logout_view'),
    path('delete', delete_view, name='delete_view'),
    path('like', like_view, name='like_view')
]
