from django.shortcuts import render, redirect
from django.http import JsonResponse
from contact.forms import MessageForm
from works.models import Work, WorkCategore
from servecs.models import Service
from blogs.models import News, Category
from contact.models import Contact
# Create your views here.


def home(request):
    contacts = Contact.objects.get()
    services = Service.objects.all()
    categore_btn = request.GET.get('categore_btn') 
    if categore_btn: 
        work = Work.objects.filter(id=categore_btn).order_by('-created_at')
    else:
        work = Work.objects.all().order_by('-created_at') 
    categore = WorkCategore.objects.all()
    context = {
        'work': work,
        'categore': categore,
        'services':services,
        'contacts':contacts
    }
    return render(request, 'pages/home.html', context)



def works(request):
    contacts = Contact.objects.get()
    categore_btn = request.GET.get('categore_btn') 
    if categore_btn: 
        work = Work.objects.filter(id=categore_btn).order_by('-created_at')
    else:
        work = Work.objects.all().order_by('-created_at') 
    categore = WorkCategore.objects.all()
    context = {
        'work': work,
        'categore': categore,
        'contacts':contacts
    }
    return render(request, 'pages/works.html', context)

def workone(request, id):
    contacts = Contact.objects.get()
    works = Work.objects.get(id=id)
    context = {
        'work':works,
        'contacts':contacts
    }
    return render(request, 'include/work.html', context)



def servec(request):
    contacts = Contact.objects.get()
    services = Service.objects.all()
    context = {
        'services':services,
        'contacts':contacts
    }
    return render(request, 'pages/servec.html', context)


def blogs(request):
    contacts = Contact.objects.get()
    categore_btn = request.GET.get('categore_btn')
    topic = request.GET.get('topic')
    categore = Category.objects.all()
    if categore_btn:
        blog = News.objects.filter(id=categore_btn).order_by('-created')
    elif topic:    
        blog = News.objects.filter(title__icontains=topic).order_by('-created')
    else:
        blog = News.objects.all().order_by('-created')
    context = {
        'categore':categore,
        'blog':blog,
        'contacts':contacts
    }
    return render(request, 'pages/blogs.html', context)

def blogone(request, id):
    contacts = Contact.objects.get()
    blog = News.objects.get(id=id)
    return render(request, 'include/blog.html', {'blog':blog, 'contacts':contacts})


def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('HX-Request'):
                return JsonResponse({'message': 'Xabar muvaffaqiyatli yuborildi!'})
            return redirect('message_form')
    return JsonResponse({'message': 'Xato!'}, status=400)