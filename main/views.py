from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models

def index(request):
    context = {}
    return render(request, 'conf/index.html', context)


def contact(request):
    if request.method == 'POST':
        models.Form.object.create(
            body = request.POST['body'],
            name = request.POST['name'],
            email = request.POST['email']
        )
#        return redirect('index')
    return render(request, 'conf/contact.html')

def news(request):
    category_id = request.GET.get('category_id')
    categorys = models.Category.objects.all().order_by('name')

    if category_id:
        category = models.Category.objects.get(id = category_id)
        news = models.Item.objects.filter(category=category, is_active=True)
        satus = category
    else:
        satus = 0
        news = models.Item.objects.filter(is_active = True)

    context = {
        'news':news,
        'categorys':categorys,
        'satus':satus
    }
    return render(request, 'conf/news.html',context)

# dashboard

def dashboard(request):
    users = User.objects.all().count()
    news = models.Item.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'news':news,
        'regions':regions,
        'category':category
    }

    return render(request, 'dashb/index.html', context)

#                                                    region CRUD

def create_region(request):
    if request.method == 'POST':
        models.Region.objects.create(
            name=request.POST['name']
        )
        return redirect('regions')
    return render(request, 'dashb/region/create.html')


def regions(request):
    regions = models.Region.objects.all()
    return render(request, 'dashb/region/list.html', {'regions':regions})



def region_update(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        return redirect('regions')
    return render(request, 'dashb/region/update.html', {'region':region})


def region_delete(request, id):
    models.Region.objects.get(id=id).delete()
    return redirect('regions')


#                                                       category CRUD
def create_category(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categorys')
    return render(request, 'dashb/category/create.html')


def categorys(request):
    categorys = models.Category.objects.all()
    return render(request, 'dashb/category/list.html', {'categorys':categorys})


def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('regions')
    return render(request, 'dashb/category/update.html', {'category':category})


def category_delete(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('category')


#item

def create_item(request):
    if request.method == 'POST':
        title=request.POST['title']
        body=request.POST['body']
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])
        image = request.FILES['image']

        models.Item.objects.create(
            title=title,
            body=body,
            category=category,
            region=region,
            image=image
    )
        return redirect('items')
    context = {
        'categorys':models.Category.objects.all(),
        'regions':models.Region.objects.all()
    }
    return render(request, 'dashb/items/create.html',context)


def items(request):
    items = models.Item.objects.all()
    context  = {
        'items':items,

    }
    return render(request, 'dashb/items/list.html', context)



def item_update(request, id):
    item = models.Item.objects.get(id=id)
    if request.method == 'POST':
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])
        item.title = request.POST['title']
        item.body = request.POST['body']
        item.category=category
        item.region=region
        image = request.FILES.get('image')
        if image:
            item.image=image
        item.save()

    context  = {
        'item':item,
        'categorys':models.Category.objects.all(),
        'regions':models.Region.objects.all()
    }

    return render(request, 'dashb/items/update.html', context)


def item_delete(request, id):
    models.Item.objects.get(id=id).delete()
    return redirect('items')


#form


def create_form(request):
    if request.method == 'POST':
        models.Form.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            body=request.POST['body'],
            email = request.POST.get('email')
        )
        return redirect('forms')
    return render(request, 'dashb/form/create.html')


def forms(request):
    forms = models.Form.objects.all()
    return render(request, 'dashb/form/list.html', {'forms':forms})


def form_update(request, id):
    form = models.Form.objects.get(id=id)
    if request.method == 'POST':
        form.name = request.POST['name']
        form.phone = request.POST['phone']
        form.body = request.POST['body']
        form.email = request.POST['email']
        form.save()
        return redirect('forms')
    return render(request, 'dashb/form/update.html', {'form':form})


