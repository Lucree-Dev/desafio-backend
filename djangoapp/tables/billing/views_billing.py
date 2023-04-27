from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import BillingCard
from ...serializers import BillingCardSerializer

"""
GET /account/BillingCards
Methods: get, post, put, update and delete
"""

#get all BillingCards
@api_view(['GET'])
def getBillingCards(request):
    billing = BillingCard.objects.all()
    serial = BillingCardSerializer(billing, many=True)
    return Response(serial.data)

#get single BillingCards
@api_view(['GET'])
def getBillingCard(request, pk):
    billing = BillingCard.objects.get(id=pk)
    serial = BillingCardSerializer(billing, many=False)
    return Response(serial.data)

#add BillingCards
@api_view(['POST'])
def addBillingCard(request):
    serial = BillingCardSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update BillingCards
@api_view(['PUT'])
def updateBillingCard(request, pk):
    billing = BillingCard.objects.get(id=pk)
    serial = BillingCardSerializer(instance=billing, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete BillingCards
@api_view(['DELETE'])
def deleteBillingCard(request, pk):
    billing = BillingCard.objects.get(id=pk)
    billing.delete()
    
    return Response('Item successfully deleted!')