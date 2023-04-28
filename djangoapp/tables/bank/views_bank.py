from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import BankStatement
from ...serializers import BankStatementSerializer

"""
GET /account/BankStatements
Methods: get, post, put, update and delete
"""

#get all BankStatements
@api_view(['GET'])
def getBankStatements(request):
    bank = BankStatement.objects.all()
    serial = BankStatementSerializer(bank, many=True)
    return Response(serial.data)

#get single BankStatements
@api_view(['GET'])
def getBankStatement(request, pk):
    bank = BankStatement.objects.get(id=pk)
    serial = BankStatementSerializer(bank, many=False)
    return Response(serial.data)

#add BankStatements
@api_view(['POST'])
def addBankStatement(request):
    serial = BankStatementSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update BankStatements
@api_view(['PUT'])
def updateBankStatement(request, pk):
    bank = BankStatement.objects.get(id=pk)
    serial = BankStatementSerializer(instance=bank, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete BankStatements
@api_view(['DELETE'])
def deleteBankStatement(request, pk):
    bank = BankStatement.objects.get(id=pk)
    bank.delete()
    
    return Response('Item successfully deleted!')