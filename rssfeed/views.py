from django.shortcuts import render
from .models import Feed,Home,Folder
from django.views.generic import ListView,DetailView, TemplateView
import feedparser
from .rss_helper import get_rss_data
from .save_object import save_obj

# Create your views here.

class AllFeedView(TemplateView):
    template_name = 'rssfeed/all.html'

    def collate_feeds(self,feeds):
        collated_feeds= []
        for feed in feeds:
            fetched_feed = get_rss_data(feed.feed_url)
            if fetched_feed:
                for item in fetched_feed:
                    item['feed_name'] = feed.name
                    collated_feeds.append(item)

        save_obj(collated_feeds)
        sorted_feeds = sorted(collated_feeds, key=lambda x: x['formatted_date'],reverse=True)
        return sorted_feeds

    def get_context_data(self, **kwargs):
        feeds = Feed.objects.all()
        collated_feeds = self.collate_feeds(feeds)
        context = super().get_context_data(**kwargs)
        context['feeds'] = collated_feeds

        return context

class FeedDetails(DetailView):
    model = Feed
    context_object_name = 'selected_feed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.object.feed_url
        feeds = get_rss_data(url)
        sorted_feeds = sorted(feeds, key=lambda x: x['formatted_date'],reverse=True)
        context['feed_details'] = sorted_feeds

        
        return context


class HomeView(TemplateView):
    template_name = 'rssfeed/index.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_details'] = Home.objects.all()

        return context
