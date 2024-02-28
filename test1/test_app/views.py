from django.shortcuts import render , redirect
from test_app.forms import searchForm, testForm

from test_app.models import TestModel

# Create your views here.
def index(req):
    ob = TestModel.objects.all()
    return render (req,"index.html",{'ob':ob})

def search(req):
    if req.method == 'GET':
        form = searchForm(req.GET)
        if form.is_valid():
            query = form.cleaned_data.get('search_q')
            results = TestModel.objects.filter(student_id=query)

        else:
            results = TestModel.objects.all()

    else:
        form = searchForm()
        results = TestModel.objects.all()

    return render(req,'search.html' ,{'form': form, 'results': results})


def update(req,id):
    ob = TestModel.objects.get(pk=id)
    form = testForm(req.POST,instance=ob)
    if form.is_valid():
        form.instance.owner = req.user
        form.save()
        return redirect('/')
    return render(req,'update.html',{'wicha':ob})

def delete_item(req, id):
    item = TestModel.objects.get(pk=id)
    item.delete()
    return redirect(search)