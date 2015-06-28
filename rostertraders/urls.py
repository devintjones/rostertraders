from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	#url(r'^login/$', 'django.contrib.auth.views.login'),
	#url(r'^logout/$', 'django.contrib.auth.views.logout'),
	#url(r'^players','app1.views.player_vals'),
	url(r'^$', 'home.views.index'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^logout/$', 'home.views.logout'),
	url(r'^contact/$','home.views.contact'),
	#url(r'^sell_shares/$', 'app1.views.sell_shares'),
	#url(r'^buy_shares/$', 'app1.views.buy_shares'),
	url(r'^admin/', include(admin.site.urls)),
]
