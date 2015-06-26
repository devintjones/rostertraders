from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf.urls.static import static

from rostertraders import home

urlpatterns = [
	#url(r'^login/$', 'django.contrib.auth.views.login'),
	#url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^players','app1.views.player_vals'),
	url(r'^$', 'rostertraders.home.views.index'),
	#url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^contact/$','app1.views.contact'),
	url(r'^logout/$', 'app1.views.logout'),
	url(r'^sell_shares/$', 'app1.views.sell_shares'),
	url(r'^buy_shares/$', 'app1.views.buy_shares'),
	url(r'^admin/', include(admin.site.urls)),
]
