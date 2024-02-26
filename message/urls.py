from django.urls import path
from . import views

urlpatterns = [
    # path('tweet', views.Tweet, name='send_tweet'),
    path('tweets', views.AllTweetList.as_view(), name='alltweets'),
    path('mytweets', views.MyTweets.as_view(), name='mytweets'),
    # path('tweet/detail/', views.TweetDetail, name='tweet_detail'),
    path('send', views.SendMessage, name='sendmessage'),
    path('', views.MessageList.as_view(), name='messages'),
    # path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    # path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    # path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    # path('view/<str:scripture>/', views.view_verse, name='view_verse'),
    # path('', views.current_date_devotional, name='daily'), 

]
