from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	url(r'^dashboard','dashboard.views.dashboard'),
	url(r'^sell_shares/$', 'dashboard.views.sell_shares'),
	url(r'^buy_shares/$', 'dashboard.views.buy_shares'),
	url(r'^player/(?P<player_id>[0-9]+)/$', 'players.views.player_page'),	
	url(r'^$', 'home.views.index'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^logout/$', 'home.views.logout'),
	url(r'^contact/$','home.views.contact'),
	url(r'^admin/', include(admin.site.urls)),
]
