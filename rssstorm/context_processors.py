from rssfeed.models import Feed, Folder, Home

# Used in base.html for the sidebar
def context_feed(request):
    feed_links = Feed.objects.all()
    return {
        "context_feed_links": feed_links
    }

def context_folder(request):
    folders = Folder.objects.prefetch_related('children','sub_folders')
    return {
        "context_folders": folders
    }

def context_home(request):
    home_properties = Home.objects.first()
    return {
        "context_home_properties": home_properties
    }
