from django.urls import path

from . import views
app_name='tourapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('add/',views.add_toy,name='add_toy'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]