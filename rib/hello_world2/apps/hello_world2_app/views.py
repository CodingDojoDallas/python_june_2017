from django.shortcuts import render

def index(request):
	print "This is inseide the index method"
	return render(request, 'hello_world2_app/index.html')
