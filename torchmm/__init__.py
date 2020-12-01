
name = "torchmm"
__version__ = "0.0.2 alpha"
authors = "Abdul Waheed, Ganeshan Malhotra"
emails = "abdulwaheed1513@gmail.com, ganeshanmalhotra@gmail.com"

__doc__ = """
    Create portable serialized representations of Python objects.

    See module copyreg for a mechanism for registering custom picklers.
    See module pickletools source for extensive comments.

    Classes:

        Pickler
        Unpickler

    Functions:

        dump(object, file)
        dumps(object) -> string
        load(file) -> object
        loads(string) -> object

    Misc variables:

        __version__
        format_version
        compatible_formats
"""