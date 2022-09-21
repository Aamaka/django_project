from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from my_app.models import Book, Publisher
from my_app.serializer import BookSerializer, PublisherSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_details(request, pk):
    # try:
    # book = Book.objects.get(isbn=pk)
    query_set = get_object_or_404(Book, isbn=pk)
    if request.method == 'GET':
        serializer = BookSerializer(query_set, context={'request': request})
        return Response(serializer.data)
    elif request.method == ('PUT', 'PATCH'):
        serializer = BookSerializer(query_set, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # except Book.DoesNotExist:
        # return Response('error: could not find resource', status=status.HTTP_404_NOT_FOUND)


@api_view()
def publisher_list(request):
    queryset = Publisher.objects.all()
    serializer = PublisherSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def publisher_details(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    except Publisher.DoesNotExist:
        return Response({"error": "could not find resource"}, status=status.HTTP_404_NOT_FOUND)

#
#
# def index(request):
#     context = [1, 4, 6, 7]
#     text = "Amaka is a girl unf jnrkdnd jendn jenknd nekni jikni"
#     return render(request, 'my_app/index.html',
#                   context={'abc': context, 'name': "Amaka", 'is_major': True, 'text': text})
#
#
# def about(request):
#     return render(request, 'my_app/about.html')
#
#
# def redirect(request):
#     print(reverse('my_app:redirect_to_about'))
#     return HttpResponseRedirect(reverse('my_app:redirect_to_about'))
#
#
# def book_list(request):
#     # books = Book.objects.all()
#     # books = Book.objects.filter(genre='FICTION')
#     #  books = Book.objects.filter(price__gt=50.00)
#     books = Book.objects.filter(publisher_id__in=(1, 7, 3)).order_by('-title', 'price').reverse()
#     # cursor = connection.cursor()
#     # result = cursor.execute("select * from my_app_book")
#     # books = result.fetchall()
#     # cursor.close()
#     # books = Book.objects.raw("select * from my_app_book ")
#     # books = Book.objects.filter(publisher_id__in=(1, 7, 3)).only('title')
#     return render(request, 'my_app/book-list.html', {'books': list(books)})
#
#
# def book_detail(request, pk):
#     # try:
#     #     book = Book.objects.get(pk = pk)
#     #     return render(request, 'my_app/book-detail.html', {'book' : book})
#     # except Book.DoesNotExist:
#     #     return HttpResponse("Good bye")
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'my_app/book-detail.html', {'book': book})
#
