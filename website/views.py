from django.shortcuts import render, redirect
from website.forms import ReserveForm

# Create your views here.


def index_website(request):
    return render(request, 'index_website.html')

def reserve_website(request):
    if request.method == 'GET':
        form = ReserveForm
    else:
        form = ReserveForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # comment = form.cleaned_data["comment"]
            # article = Article.objects.get(id=id)
            # c = Comment(name=name, comment=comment, belong_to=article)
            # c.save()
            return redirect(to="index_website")
    context = {}
    context['form'] = form
    return render(request, 'reserve_website.html', context)

def search_website(request):
    return render(request, 'search_website.html')
