from rest_framework import serializers
from app.models.company_file_upload import CompanyFileUpload


class CompanyFileUploadSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M:%S", read_only=True)

    # list_of_uploaded_file_object = []

    # def create(self, validated_data):
    #     for i in self.context.get('request').FILES.getlist('data_file'):
    #         print(f"************************* File name is {i.name}")

    #         uploaded_file_instance = CompanyDirectoryFilesUpload(
    #             name=i.name, directory="put_the_name_here_when_the_front_end_sends_that_field", data_file=i, )

    #         uploaded_file_instance.save()

    #         list_of_uploaded_file_object.append(uploaded_file_instance)

    #     return list_of_uploaded_file_object

    class Meta:
        model = CompanyFileUpload
        fields = ["id",
                  "name",
                  "user",
                  "data_file",
                  "comment",
                  "file_size",
                  "timestamp"]

        extra_kwargs = {
            'file_size': {'read_only': True},
            'name': {'read_only': True}
        }
