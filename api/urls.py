from django.urls import path
from .views import RegisterView, LoginView
from .views import UserProfileView
from .views import UserSearchView
from .views import send_friend_request
from .views import respond_to_friend_request
from .views import FriendListView
from .views import PendingRequestsView


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/', send_friend_request, name='send-friend-request'),
    path('friend-respond/', respond_to_friend_request, name='respond-to-friend-request'),
    path('friend-list/', FriendListView.as_view(), name='friend-list'),
    path('pending-requests/', PendingRequestsView.as_view(), name='pending-requests'),
    
]
