from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('news', views.news, name='news'),
        # dashboard
    path('dashb', views.dashboard),
    path('dashb/region/create', views.create_region, name='create_region'),
    path('dashb/region/list', views.regions, name='regions'),
    path('dashb/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashb/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    #category
    path('dashb/category/create', views.create_category, name='create_category'),
    path('dashb/category/list', views.categorys, name='categorys'),
    path('dashb/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashb/category/delete/<int:id>/', views.category_delete,name='category_delete'),
    #item
    path('dashb/items/create', views.create_item, name='create_item'),
    path('dashb/items/list', views.items, name='items'),
    path('dashb/items/update/<int:id>/', views.item_update, name='item_update'),
    path('dashb/items/delete/<int:id>/', views.item_delete,name='item_delete'),
    #form
    path('dashb/form/create', views.create_form, name='create_form'),
    path('dashb/form/list', views.forms, name='forms'),
    path('dashb/form/update/<int:id>/', views.form_update, name='form_update'),

]