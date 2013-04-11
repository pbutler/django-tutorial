# Create your views here.


from blog.models import Entry
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone


def list(request):
    entries = Entry.objects.all()
    context = {'entries': entries}
    return render(request, 'blog/list.html', context)


def detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'blog/detail.html', context)


def comment(request, entry_id):
    e = get_object_or_404(Entry, pk=entry_id)
    try:
        e.comment_set.create(name=request.POST['name'],
                             subject=request.POST['subject'],
                             pub_date=timezone.now(),
                             body=request.POST['body'])
    except (KeyError):
        # Redisplay the poll voting form.
        return render(request, 'blog/detail.html', {
            'entry': e,
            'error_message': "You screwed up.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect("/blog/entry/%s/" % entry_id)
