from django.shortcuts import render

def index(request):
	print "Inside the index method"

	return render(request, 'portfolio2_app/index.html')

def testimonials(request):
	print "Inside the testimonials method"

	return render(request, 'portfolio2_app/testimonials.html')
