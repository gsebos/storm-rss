from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.HomeView.as_view(), name = 'home-view'),
	path('all',views.AllFeedView.as_view(), name = 'all-view'),
	path('feed/<slug:slug>',views.FeedDetails.as_view(),name='feed-details'),
	path('folder/<slug:slug>',views.FolderView.as_view(),name='folder-list'),
	path('update-feed-location',views.update_feed_location,name='update-feed-location')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)