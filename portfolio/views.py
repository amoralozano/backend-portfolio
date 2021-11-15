from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def aboutme_view(request):
    return render(request, 'aboutme.html')


def resume_view(request):
    return render(request, 'resume.html')


def contactme_view(request):
    return render(request, 'contactme.html')


def projects_view(request):
    return render(request, 'projects.html')
