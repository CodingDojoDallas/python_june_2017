from django.shortcuts import render
import datetime

def index(request):
	print "Inside the index method"
	context = {
		'time' : datetime.datetime.now()
	}
	return render(request, 'time_display3_app/index.html',context)




