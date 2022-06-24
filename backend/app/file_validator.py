from django.core.exceptions import ValidationError


def validate_file(data_file):
    value = str(data_file)
    filesize = 419430400
    # if not value.endswith(".pdf") and not value.endswith('doc') and not value.endswith('docx'):
    #     raise ValidationError(
    #         "Only PDF or Word file(s) can be uploaded"
    #     )
    if data_file.size > filesize:
        raise ValidationError(
            "The maximum file size that can be uploaded is 50MB"
        )
    return data_file
