from django.shortcuts import get_object_or_404, render_to_response
import models

def hello(request):
    return render_to_response('my_app/hello.html',
        {'target': 'Joe', 'names': ('Abe', 'Tom')}
    )

def hello2(request, id=None):
    target = get_object_or_404(models.Person, pk=id).name

    return render_to_response('my_app/hello.html',
        {'target': target} # fails silently for names by default
    )

