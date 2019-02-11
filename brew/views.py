from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Homebrew
from . import forms

# Create your views here.
def home(request):
    jobs = Job.objects.order_by('name')
    return render(request, 'brew/home.html',{'classes':jobs})

@login_required(login_url="/user/sign_up")
def create(request):
    form = forms.createForm()
    if request.method == "POST":
        brew = Homebrew(user=request.user)
        form = forms.createForm(request.POST,instance=brew)
        if form.is_valid():
            data = form.save(commit=True)

            return redirect('/brew/{}/{}'.format(str(data.jobs.id), str(data.id)))

        # if request.POST['title'] and request.POST['sum'] and request.POST['type']:
        #     brew = Homebrew()
        #     brew.title = request.POST['title']
        #     brew.summary = request.POST['sum']
        #     check_id = request.POST['type']
        #     brew.jobs = get_object_or_404(Job, pk=check_id)
        #     brew.user = request.user
        #     brew.save()
        #     return redirect('/brew/{}/{}'.format(str(brew.jobs.id),str(brew.id)))
        else:
            return render(request, 'brew/create.html',{'createform':form,'error': 'Something went wrong!'})
    else:
        jobs = Job.objects.order_by('name')
        form = forms.createForm()
        return render(request, 'brew/create.html', {'createform':form,})

def job(request, job_id):
    job = get_object_or_404(Job,pk=job_id)
    brews = Homebrew.objects.filter(jobs=job)
    return render(request, 'brew/job.html',{'job':job, 'brews':brews})

def detail(request, job_id, brew_id):
    brew = get_object_or_404(Homebrew,pk=brew_id)
    return render(request, 'brew/detail.html', {'brew':brew})