from rest_framework import serializers
from app.models.company_directory_upload import CompanyDirectoryFilesUpload
from app.models.user import User


class CompanyDirectoryFilesUploadSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M:%S", read_only=True)

    def validate(self, validated_data):

        list_of_uploaded_file_object = []

        uploadUserInstance = User.objects.get(
            id=self.context.get('request').data["user"])

        for i in self.context.get('request').FILES.getlist('data_file'):
            # print(f"************************* File name is {i.name}")

            uploaded_file_instance = CompanyDirectoryFilesUpload(
                name=i.name, directory="i.directory", data_file=i, user=uploadUserInstance, )

            uploaded_file_instance.save()

            list_of_uploaded_file_object.append({
                "id": uploaded_file_instance.id,
                "user": uploaded_file_instance.user.id,
                "directory_name": uploaded_file_instance.directory,
                "data_file": uploaded_file_instance.data_file.url,
                "file_size": uploaded_file_instance.file_size,
                "timestamp": uploaded_file_instance.timestamp
            })

        return {"Directory files": list_of_uploaded_file_object}

    class Meta:
        model = CompanyDirectoryFilesUpload
        fields = ["id",
                  "name",
                  "directory",
                  "user",
                  "data_file",
                  "file_size",
                  "timestamp"]

        extra_kwargs = {
            'file_size': {'read_only': True},
            'name': {'read_only': True}
        }

        # list_serializer_class = BulkCreateDirectoryFilesUploadSerializer
