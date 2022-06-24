# file: ./custom_storage/custom_azure.py
from storages.backends.azure_storage import AzureStorage 


class PublicStaticAzureStorage(AzureStorage):
    azure_container = 'static'
    expiration_secs = None


# class PublicMediaAzureStorage(AzureStorage):

class  PublicMediaAzureStorage(AzureStorage):
    location = ''
    file_overwrite = False