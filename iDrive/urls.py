from rest_framework.urlpatterns import format_suffix_patterns, include
from django.conf.urls import patterns, url, include
from iDrive import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'baruser', views.BarUserViewSet, base_name='baruser')
router.register(r'promotion', views.PromotionViewSet, base_name='promotion')
router.register(r'party', views.PartyViewSet, base_name='party')
router.register(r'partyuser', views.PartyUserViewSet, base_name='partyuser')


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    )