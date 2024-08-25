from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from .models import FriendRequest
from .serializers import FriendRequestSerializer
from rest_framework import status
from rest_framework.decorators import api_view



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
    
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserSearchView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return User.objects.filter(username__icontains=query) | User.objects.filter(email__iexact=query)
        return User.objects.none()
    
@api_view(['POST'])
def send_friend_request(request):
    from_user = request.user
    to_user_id = request.data.get('to_user_id')

    try:
        to_user = User.objects.get(id=to_user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Check if a request already exists
    if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
        return Response({'detail': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create new friend request
    request_data = {
        'from_user': from_user.id,
        'to_user': to_user.id,
        'status': 'pending'
    }
    serializer = FriendRequestSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def respond_to_friend_request(request):
    request_id = request.data.get('request_id')
    action = request.data.get('action')  # 'accept' or 'reject'

    try:
        friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
    except FriendRequest.DoesNotExist:
        return Response({'detail': 'Friend request not found.'}, status=status.HTTP_404_NOT_FOUND)

    if action == 'accept':
        friend_request.status = 'accepted'
        friend_request.save()
        return Response({'detail': 'Friend request accepted.'}, status=status.HTTP_200_OK)
    elif action == 'reject':
        friend_request.status = 'rejected'
        friend_request.save()
        return Response({'detail': 'Friend request rejected.'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)
    
class FriendListView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = User.objects.filter(received_requests__from_user=user, received_requests__status='accepted') | \
                  User.objects.filter(sent_requests__to_user=user, sent_requests__status='accepted')
        return friends
    
class PendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')
    
    

    
    

