from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Photo

def home(request):

    category = request.GET.get('cat')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category )
    
    categories = Category.objects.all()
    photos_count = photos.count()

    context = {'categories':categories, 'photos':photos, 'photos_count':photos_count}


    return render(request,'photo/home.html',context)

def addPhoto(request):
    categorys = Category.objects.all()
    context = {'categorys':categorys}
    if request.method == 'POST':
        data = request.POST
        image = request.FILES['image']

        if data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            description = data['description'],
            image = image,
            category = category
        )

        return redirect('home')



    return render(request,'photo/add.html',context)

def photoView(request,pk):
    photo = Photo.objects.get(id = pk)

    context = {'photo':photo}
    return render(request, 'photo/photo.html',context)


