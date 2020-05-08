from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.product_main, name='product_main'),
	url(r'^new/$', views.product_new, name='product_new'),
    url(r'^catalog/$', views.product_list, name='product_list'),
    url(r'^Brends/$', views.product_brends, name='product_brends'),
    url(r'^About_shop/$', views.product_shop, name='product_shop'),
    url(r'^About_sweets/$', views.product_sweets, name='product_sweets'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),

]