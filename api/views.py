from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all() 
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_BAD_REQUEST)
    
    
class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

   

    
        
