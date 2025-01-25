from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.HomeView.as_view(), name = 'home-view'),
	path('all',views.AllFeedView.as_view(), name = 'all-view'),
	path('<int:pk>',views.FeedDetails.as_view(),name='feed-details')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)