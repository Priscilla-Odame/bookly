from rest_framework import serializers
from app.models.file_upload import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = FileUpload
        fields = ["id", "user", "project", "data_file",
                  "file_size", "title", "timestamp"]

        extra_kwargs = {
            'file_size': {'read_only': True},
        }
