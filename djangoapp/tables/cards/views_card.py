from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Card
from ...serializers import CardSerializer

"""
GET /account/Cards
Methods: get, post, put, update and delete
"""

#get all Cards
@api_view(['GET'])
def getCards(request):
    card = Card.objects.all()
    serial = CardSerializer(card, many=True)
    return Response(serial.data)

#get single Cards
@api_view(['GET'])
def getCard(request, pk):
    card = Card.objects.get(id=pk)
    serial = CardSerializer(card, many=False)
    return Response(serial.data)

#add Cards
@api_view(['POST'])
def addCard(request):
    serial = CardSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update Cards
@api_view(['PUT'])
def updateCard(request, pk):
    card = Card.objects.get(id=pk)
    serial = CardSerializer(instance=card, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete Cards
@api_view(['DELETE'])
def deleteCard(request, pk):
    card = Card.objects.get(id=pk)
    card.delete()
    
    return Response('Item successfully deleted!')