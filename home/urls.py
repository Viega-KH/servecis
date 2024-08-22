from django.urls import path
from .views import home, works, servec, blogs, workone, blogone, submit_message

urlpatterns = [
    path('', home, name='home'),
    path('works/', works, name='works'),
    path('workone/<int:id>', workone, name='workone'),
    path('serves/',  servec, name='servec'),
    path('blogs/',  blogs, name='blogs'),
    path('blogone/<int:id>',  blogone, name='blogone'),
    path('message/submit/', submit_message, name='submit_message'),
]
