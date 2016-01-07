from django.conf.urls import url

from . import views

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^index$', views.index, name='index'),

    url( r'^groups/home$', views.groups_home, name='groups_home'),
    url( r'^groups/add$', views.groups_add, name='groups_add'),
    url( r'^groups/add_action$', views.groups_add_action, name='groups_add_action'),
    url( r'^groups/list$', views.groups_list, name='groups_list'),
    url( r'^groups/csv$', views.groups_csv, name='groups_csv'),


    url( r'^customers/home$', views.customers_home, name='customers_home'),
    url( r'^customers/add$', views.customers_add, name='customers_add'), 
    url( r'^customers/add_action$', views.customers_add_action, name='customers_add_action'),
    url( r'^customers/list$', views.customers_list, name='customers_list'), 
    url( r'^customers/detail/(?P<customerid>[0-9])$', views.customers_detail, name='customers_detail'), 
    url( r'^customers/csv$', views.customers_csv, name='customers_csv'), 


    url( r'^orders/home$', views.orders_home, name='orders_home'),
    url( r'^orders/add$', views.orders_add, name='orders_add'), 
    url( r'^orders/add_action$', views.orders_add_action, name='orders_add_action'),
    url( r'^orders/list$', views.orders_list, name='orders_list'),
    url( r'^orders/csv$', views.orders_csv, name='orders_csv'),
    

    url( r'^rewards/home$', views.rewards_home, name='rewards_home'),
    url( r'^rewards/add$', views.rewards_add, name='rewards_add'), 
    url( r'^rewards/add_action$', views.rewards_add_action, name='rewards_add_action'),
    url( r'^rewards/list$', views.rewards_list, name='rewards_list'),
    url( r'^rewards/csv$', views.rewards_csv, name='rewards_csv'),
    

]

