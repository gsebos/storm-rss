from django.shortcuts import render
from .models import Feed,Home,Folder
from django.views.generic import ListView,DetailView, TemplateView
import feedparser
from .rss_helper import get_rss_data
from .save_object import save_obj
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

@csrf_protect  # Ensure CSRF protection is enabled
def update_feed_location(request):
    if request.method == 'POST':
         # Parse JSON data from request.body
        try:
            data = json.loads(request.body)  # Convert the body from JSON string to a Python dictionary
            django_model = data.get('django_model')  # Extract selected_id from the parsed data
            django_operation = data.get('django_operation')  # Extract selected_folder_id
            new_foreignKey = data.get('new_foreignKey')  # Extract selected_folder_id
            item_pk = data.get('item_pk')  # Extract selected_folder_id

            print(f"django_operation ID: {django_operation}, new_foreignKey: {new_foreignKey}")

            # Your logic to handle the data
            # print(f"django_model: {django_model}, django_operation: {django_operation}")
            if django_operation == 'Update_ForeignKey':

                new_folder = Folder.objects.get(pk=new_foreignKey)

                if django_model == 'Feed':
                    feed = Feed.objects.get(pk=item_pk)
                    feed.folder = new_folder
                    feed.save()
                    
                if django_model == 'Folder':
                    folder = Folder.objects.get(pk=item_pk)
                    folder.parent_folder = new_folder
                    folder.save()
                
            if django_operation == 'ForeignKey_to_blank':

                if django_model == 'Feed':
                    feed = Feed.objects.get(pk=item_pk)
                    print(feed)
                    feed.folder = None
                    feed.save()
                    
                if django_model == 'Folder':
                    folder = Folder.objects.get(pk=item_pk)
                    folder.parent_folder = None
                    folder.save()

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        
        # Return a JSON response
        return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

        
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


class FolderView(TemplateView):
        model = Folder
        template_name = 'rssfeed/folder.html'

class HomeView(TemplateView):
    template_name = 'rssfeed/index.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_details'] = Home.objects.all()

        return context
