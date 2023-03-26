from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    # The home page for Learning Log again #
    return render(request, 'learning_log_again/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log_again/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log_again/topic.html', context)
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log_again:topics')
    context = {'form': form}
    return render(request, 'learning_log_again/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_log_again:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log_again/new_entry.html', context)

