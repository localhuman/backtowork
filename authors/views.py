from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

from .forms import TweetForm
from .models import Author

@login_required()
def home(request):

    authors = Author.objects.all()

    return render(request, 'home.html',locals())

@login_required()
def author_detail(request, pk):

    author = get_object_or_404(Author,pk=pk)

    authors = Author.objects.all()

    return render(request, 'home.html', locals())


@login_required()
def author_tweet(request):

    if request.POST:

        form = TweetForm(request.POST)

        if form.is_valid():

            author = form.cleaned_data['sent_by']
            reply_to = form.cleaned_data['reply_to']

            tweet = author.compose_tweet(at=reply_to)
            print("tweet: %s " % tweet)
            result = author.send_tweet(tweet)
            print("result: %s " % result)

            messages.add_message(request, messages.INFO, 'Sent Tweet %s' % tweet)

    return HttpResponseRedirect('/')

@login_required()
def follow_authors(request, pk):
    author = get_object_or_404(Author, pk=pk)

    all_authors = Author.objects.all().exclude(pk=pk)

    res = author.sync_author_followers(all_authors)

    messages.add_message(request, messages.INFO, 'Sync authors: %s ' % res)

    return HttpResponseRedirect('/')

