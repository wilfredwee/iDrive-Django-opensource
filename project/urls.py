from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import views
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('iDrive.urls')),
                       url(r'^home/', views.home, name='home'),
                       url(r'^business/', views.business, name='business'),
                       url(r'^promotions/', views.promotions, name='promotions'),
                       url(r'^login/', views.login, name='login'),
                       url(r'^logout/', views.logout, name='logout'),
                       url(r'^create_promotion/', views.create_promotion, name="create_promotion"),
                       url(r'^current_promotions/', views.current_promotions, name="current_promotions"),
                       url(r'^sign_up/', views.sign_up, name="sign_up"),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),
                       )