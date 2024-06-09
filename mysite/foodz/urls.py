from . import views

from django.urls import path

app_name = 'foodz'
urlpatterns = [
    #/foodz/
    path('', views.IndexClassView.as_view(),name='index'),
    #/foodz/1
    path('<int:pk>/',views.FoodzDetail.as_view(),name='detail'), 
    path('items/',views.items,name='items'),
    # add items 
    path('add',views.CreateItems.as_view(),name='create_items'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]