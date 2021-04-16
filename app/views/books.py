from django.shortcuts import render
from app.submodels.books import Book
from app.serializers.books import BooksSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse


class BookViews(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filterset_fields = ['title', 'author']

    def post(self,request):
        file_model = Book()
        
        _, file = request.FILES.popitem() #get first element of uploaded images
        file = file[0] # get the file from MultiValueDict

        file_model.file = file
        file_model.save()

        return HttpResponse(content_type='text/plain', content='File added')

# class FileUpload(viewsets.ModelViewSet):
#     #permission_classes = (IsAdminUser, IsAuthenticated)

#     serializer_class = BooksSerializer
#     queryset = Book.objects.all()

#     def post(self,request):
#         file_model = Book()
        
#         _, file = request.FILES.popitem() #get first element of uploaded images
#         file = file[0] # get the file from MultiValueDict

#         file_model.file = file
#         file_model.save()

#         return HttpResponse(content_type='text/plain', content='File added')

def books(request):
    # all_books = Book.objects.all()
    # filterset_fields = ['title','author']
    # args = {'all_books': all_books}
    return render(request,'books.html')