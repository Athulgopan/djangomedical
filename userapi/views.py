from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm
from tablemedicine.forms import ProductForm
from .serializers import useapiSerializer
from tablemedicine.models import medkit
from django.shortcuts import get_object_or_404



# SIGN UP PAGE
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# LOGIN PAGE

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    response_data = {
    'message': 'Logged in as  ' + username,'token': token.key
    
}
    return Response(response_data, status=HTTP_200_OK)

# IMPORTING STOCK
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_medic(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response("successfully  save to Data base ", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_medic(request, pk):
    product = get_object_or_404(medkit, pk=pk)
    form = ProductForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = useapiSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_product(request, pk):
    try:
        product = medkit.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listmed(request):
    product = medkit.objects.all()
    serializer = useapiSerializer(product,many=True)
    return Response(serializer.data)

@api_view([ 'POST'])
@permission_classes((IsAuthenticated,))
def searchmed(request):
    medicname = request.data.get('name')  
    products = medkit.objects.filter(MedicineName__icontains=medicname)
    if products.exists():
        serializer = useapiSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response("no med available", status=status.HTTP_404_NOT_FOUND)










