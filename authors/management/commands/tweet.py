from __future__ import unicode_literals
from authors.models import Author,RepliedTo

from django.core.management.base import BaseCommand,CommandError
import time
import pprint
class Command(BaseCommand):

    help = 'reply to dt tweet'

    def handle(self, *args, **options):


        author = Author.objects.get(pk=1)

        dtweets = author.api.GetUserTimeline(screen_name='realDonaldTrump',count=20)

        for dt in dtweets:
            id = dt.id
            text = dt.text


            tweets = RepliedTo.objects.filter(twitter_id=id)

            if len(tweets):
                print("already replide to: %s \n" % text)
            else:
                tweet = author.get_tweet()
                print("Will tweet: %s " % tweet)

                result = author.api.PostUpdate(tweet, in_reply_to_status_id=id)

                savetweet = RepliedTo.objects.create(twitter_id=id)
                savetweet.save()
#                print("saved tweet: %i " % savetweet.twitter_id)
                break



        print("Complete")

