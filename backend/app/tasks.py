import io, math
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from django.core.files.storage import FileSystemStorage
from django.core.files.images import ImageFile
from rest_framework.response import Response
from app.read_chunk import read_chunk


@shared_task(bind=True)
def progress_upload(self, image_file, length, data, user, object_model=None, model_instance=None):
    """
    create a celery task to upload a file, while also keeping a progress state of the upload
    :param self:
    :param image_file: the file to be uploaded
    :param length: the size of the chunk size
    """
    process_recoder = ProgressRecorder(self)
    print('Upload progress Init..')
    fs = FileSystemStorage()
    buffer = io.BytesIO()
    chunk_size = 0
    for chunk in read_chunk(image_file.file, length):
        chunk_size += 1
        buffer.write(chunk)
        if chunk_size == 1:
            length = math.ceil((len(image_file.file.getvalue())) / length)
        process_recoder.set_progress(chunk_size, length, description=f'Uploaded {chunk_size*length} bytes of the file')
    buffer.seek(0)
    image = io.BytesIO(buffer.getvalue())
    image_file = ImageFile(image, name=image_file.name)
    if object_model is not None:
        file_upload = model_instance.objects.create(user=user, project=object_model, data_file=image_file, title=data['title'])
    else:
        file_upload = model_instance.objects.create(name=data['name'], user=user, data_file=image_file, comment=data['comment'])
    file_upload.save()
    return 'Done'
