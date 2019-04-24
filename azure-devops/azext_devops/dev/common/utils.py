# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def open_file(filepath):
    import subprocess
    import platform
    import os
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def delete_dir(path):
    import shutil
    shutil.rmtree(path)


def randomword(length):
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# Decorators

def singleton(myclass):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = myclass(*args, **kwargs)
        return instance[0]
    return wrapper
