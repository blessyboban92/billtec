from django.urls import path,include

from . import views
app_name='credentails'
urlpatterns = [
    path('',views.sregister,name='sregister'),
    path('register/',views.searchindex,name='searchindex'),
    path('register/<int:reg_id>/',views.detail,name='registerdetail')


]