from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Transfer
from ...serializers import TransferSerializer

"""
GET /account/Transfers
Methods: get, post, put, update and delete
"""

#get all Transfers
@api_view(['GET'])
def getTransfers(request):
    transfer = Transfer.objects.all()
    serial = TransferSerializer(transfer, many=True)
    return Response(serial.data)

#get single Transfers
@api_view(['GET'])
def getTransfer(request, pk):
    transfer = Transfer.objects.get(id=pk)
    serial = TransferSerializer(transfer, many=False)
    return Response(serial.data)

#add Transfers
@api_view(['POST'])
def addTransfer(request):
    serial = TransferSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update Transfers
@api_view(['PUT'])
def updateTransfer(request, pk):
    transfer = Transfer.objects.get(id=pk)
    serial = TransferSerializer(instance=transfer, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete Transfers
@api_view(['DELETE'])
def deleteTransfer(request, pk):
    transfer = Transfer.objects.get(id=pk)
    transfer.delete()
    
    return Response('Item successfully deleted!')