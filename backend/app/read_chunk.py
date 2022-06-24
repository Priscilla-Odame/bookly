import os


def read_chunk(file_object, chunk_size=125):
    """
    read files in chunks in a generative manner,
    instead of loading the entire files into memort,
    the function takes in a file objects (eg. image video),
    and a chunk size, which defaults to 10000 bytes e.g 10kb
    """

    while True:
        file = file_object.read(chunk_size)
        if not file:
            break
        yield file
