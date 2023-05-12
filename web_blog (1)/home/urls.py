from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cntact/',views.cntact,name='contact'),
    path('about/',views.about,name='about'),
    path('code/',views.code,name='code'),
    path('compiler/',views.comp,name='comp'),
    path('search/',views.search,name='search'),
    path('signin/',views.signup,name='signup'),
]
