from django.conf.urls import url, include
from . import views


urlpatterns=[
    url('^$',views.index,name= 'index'),
     url('^profile/$', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(\d+)',views.comment,name ='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    # url(r'^logout/$', views.logout, {"next_page": '/'}),
    
    url(r'^profile/$', views.new_profile, name='new_profile')
]
