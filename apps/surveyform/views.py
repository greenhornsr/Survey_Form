from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    counter = 0
    return render(request, 'surveyform/index.html')

def process(request):
    if request.method=='POST':
        request.session['name'] = request.POST['name']
        request.session['dojoloc'] = request.POST['dojoloc']
        request.session['favlang'] = request.POST['favlang']
        request.session['comments'] = request.POST['comments']
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    request.session['counter']+=1
    return render(request, 'surveyform/result.html')
