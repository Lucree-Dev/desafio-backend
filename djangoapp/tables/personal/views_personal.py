from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Personal
from ...serializers import PersonalSerializer


"""
POST /account/person
Methods: get, post, put, update and delete
"""

#get all persons
@api_view(['GET'])
def getPersonals(request):
    personal = Personal.objects.all()
    serial = PersonalSerializer(personal, many=True)
    return Response(serial.data)

#get single person
@api_view(['GET'])
def getPersonal(request, pk):
    person = Personal.objects.get(id=pk)
    serial = PersonalSerializer(person, many=False)
    return Response(serial.data)

#add person
@api_view(['POST'])
def addPersonal(request):
    serial = PersonalSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#update person
@api_view(['PUT'])
def updatePersonal(request, pk):
    person = Personal.objects.get(id=pk)
    serial = PersonalSerializer(instance=person, data=request.data)
    
    if serial.is_valid():
        serial.save()
    
    return Response(serial.data)

#delete person
@api_view(['DELETE'])
def deletePersonal(request, pk):
    person = Personal.objects.get(id=pk)
    person.delete()
    
    return Response('Item successfully deleted!')