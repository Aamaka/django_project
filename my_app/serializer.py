from rest_framework import serializers

from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    # publisher = serializers.HyperlinkedRelatedField(
    #     query_set=Publisher.objects.all(),
    #     view="book_publisher-details"

    class Meta:
        model = Publisher
        # fields = "__all__"
        fields = ["name", "email", "url"]


class BookSerializer(serializers.ModelSerializer):  # noqa
    book_title = serializers.CharField(max_length=255, source='title')

    class Meta:
        model = Book
        # fields = "__all__"
        fields = ["book_title", "description", "isbn", "price", "publisher"]
