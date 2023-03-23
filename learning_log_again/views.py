from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    # The home page for Learning Log again #
    return render(request, 'learning_log_again/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log_again/topics.html', context)