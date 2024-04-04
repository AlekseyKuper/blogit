from django.urls import path
from polls.views import *
app_name = 'polls'
urlpatterns = [
    path('results/', ResultListView.as_view(),
         name='subject_list'),
    path('results/<pk>/',
         ResultDetailView.as_view(),
         name='subject_detail'),]