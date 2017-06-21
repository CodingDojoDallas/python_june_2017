from django.shortcuts import render, redirect

def index(request):
	print "Inside the index method"
	if 'counter' not in request.session:
		request.session['counter'] = 0

	return render(request, 'survey4_app/index.html')

def process(request):
	print "Inside the process method"
	request.session['counter'] += 1
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/results')

	return redirect('/')
def results(request):
	print "Inside the results method"

	return render(request, 'survey4_app/results.html')


