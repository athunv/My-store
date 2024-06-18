from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from api.models import product,Carts,Review
from api.serializers import ProductSerializer, ProductModelSerializers,UserSerializer,CartSerializer,ReviewSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

class productView(APIView):
    def get(self,request,*args,**kw):
        qs=product.objects.all()
        serializer = ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kw):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
    
class ProductdetailsView(APIView):
    
    def get(self,request,*args,**kw):
        print(kw)
        id = kw.get("id")
        qs = Product.objects.get(id=id)
        serializer=ProductSerializer(qs,many=False)
        return Response(data=serializer.data)
    
    
    def put(self,request,*args,**kw):
        id = kw.get('id')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
       
     
    def delete(self,request,*args,**kw):
        id = kw.get('id')
        Products.objects.filter(id=id).delete()
        return Response(data='object deleted')
    
# class ProductviewsetView(ViewSet):
#     def list(self,request,*args,**kw):
#         qs = product.objects.all()
#         serializer = ProductSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args,**kwargs):
#         serializer = ProductModelSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)


#     def retrieve(self,request,*args,**kw):
#         print(kw)
#         id = kw.get("pk")
#         qs = product.objects.get(id=id)
#         serializer=ProductSerializer(qs,many=False)
#         return Response(data=serializer.data)

#     def update(self, request, *args, **kwargs):
#         id = kw.get('pk')
#         serializer = productModelSerializers(data=request.data,instance=id)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

#     def destroy(self, request, *args, **kwargs):
#             id = kw.get('pk')
#             product.object.filter(id=id).delete()
#             return Response(data='deleted')


#     @action(methods=['GET'],detail=False)
#     def categories(self,request,*args,**kw):
#         res = product.objects.values_list('catagory',flat=False).distinct()
#         return Response(data=res)

#     @action(methods=['GET'], detail=False)
#     def des(self,request,*args,**kw):
#         res = product.objects.values_list('name',flat=False).distinct()
#         return Response(data=res)

# class Userview(ViewSet):
#     def create(self,request,*args,**kw):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(serializer.errors)

class UserModelView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all


class ProductModelViewset(ModelViewSet):
    serializer_class = ProductModelSerializers
    queryset = product.objects.all()
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kw):
        
        id = kw.get("pk") 
        item = product.objects.get(id=id)
        user = request.user
        user.carts_set.create(products=item)
        return Response(data = 'item added to cart')

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kw):

        user = request.user
        id = kw.get('pk')
        object = product.objects.get(id=id)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(products=object,user=user)
            return Response(data=serializer.data)

        else:
            return Response(data=serializer.errors)


    @action(methods=["GET"],detail=True)
    def reviews(self,request,*args,**kw):

        # id = kw.get('pk')
        # products = product.objects.get(id=id)
        products = self.get_object()
        qs = products.review_set.all()
        serializer = ReviewSerializer(qs,many=True)
        return Response(serializer.data)


    

# class Cartviewset(APIView):
#     authentication_classes = [authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]

#     def post(self,request,*args,**kw):

#         id = kw.get("id")
#         item = product.objects.get(id=id)
#         user = request.user
#         user.carts_set.create(products=item)
#         return Response(data = 'item added to cart')

class Cartviewsets(ModelViewSet):
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Carts.objects.all()


    # def list(self,request, *args, **kw):

    #     qs = request.user.carts_set.all()
    #     serializer = CartSerializer(qs,many=True)
    #     return Response(data=serializer.data)

    def get_queryset(self):

        return self.request.user.carts_set.all()

class DeleteReview(APIView):

    def delete(self,request,*args,**kw):

        id = kw.get('pk')

        Review.objects.filter(id=id).delete()

        return Response(data='Review deleted')







