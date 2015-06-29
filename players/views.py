from django.shortcuts import render

from dashboard.models import Stats,Players


def player_page(request,player_id):
	
	player_stats = Stats.objects.filter(pid=player_id)
	
	player_name = Players.objects.get(pid=player_id).name

	context = {'player_stats': player_stats,
		   'player_name' : player_name}
	return render(request,'player.html',context)
