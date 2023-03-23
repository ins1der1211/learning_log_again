from django.shortcuts import render

# Create your views here.
def index(request):
    # The home page for Learning Log again #
    return render(request, 'learning_log_again/index.html')