from blogs.models import News
from works.models import Work
from servecs.models import Service
from contact.models import Contact
def global_context(request):
    return {
        'news_count': News.objects.count(),
        'work_count': Work.objects.count(),
        'services_count': Service.objects.count(),
        'contact_count': Contact.objects.count(),
    }