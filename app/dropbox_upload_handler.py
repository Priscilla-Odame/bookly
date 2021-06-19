
def file_upload_handler_view(request):
    if request.method == "POST":
        file_uploaded = request.FILES["name_of_file_input"]
        print (file_uploaded.read())
    # Helpful attribute to get dropbox file metadata
    # like path on the server, size, thumbnail etc
    file_uploaded.dropbox_metadata