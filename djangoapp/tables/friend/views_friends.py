from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Friend
from ...serializers import FriendSerializer

"""
GET /account/friends
Methods: get, post, put, update and delete
"""

#get all friends
@api_view(['GET'])
def getFriends(request):
    friend = Friend.objects.all()
    serial = FriendSerializer(friend, many=True)
    return Response(serial.data)

#get single friends
@api_view(['GET'])
def getFriend(request, pk):
    friend = Friend.objects.get(id=pk)
    serial = FriendSerializer(friend, many=False)
    return Response(serial.data)

#add friends
@api_view(['POST'])
def addFriend(request):
    serial = FriendSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update friends
@api_view(['PUT'])
def updateFriend(request, pk):
    friend = Friend.objects.get(id=pk)
    serial = FriendSerializer(instance=friend, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete friends
@api_view(['DELETE'])
def deleteFriend(request, pk):
    friend = Friend.objects.get(id=pk)
    friend.delete()
    
    return Response('Item successfully deleted!')