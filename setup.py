from distutils.core import setup, Extension
from glob import glob
from platform import platform

PYTHON_LIBRARY_PATH = (
    '/Library/Frameworks/Python.framework/Versions/2.7/lib'
    if platform() == 'Darwin'
    else ''  # TODO: Linux
)


extension_mod = Extension(
    "threaded_remote_manager",
    sources = [
        "wrapper.c",
        "functions.c"
    ],
    include_dirs = [
        # Windows
        'c:\\msys32\\usr\\local\\include\\',
        # UNIX
        'libraries/libssh2-1.7.0/include'
    ],
    library_dirs = (
        # Windows
        [
            'c:\\Python27\\libs',
            'c:\\msys32\\usr\\local\\lib',
            'c:\\msys32\\mingw32\\i686-w64-mingw32\\lib'
        ]
        if platform() == 'Windows'
        else
        # UNIX
        [
            'libraries/libssh2-1.7.0/src/.libs/',
            'libraries/openssl-1.0.2g/usr/local/openssl_build/lib',
            PYTHON_LIBRARY_PATH
        ]
    ),
    libraries = (
        # Windows
        ['python27', 'ssh2', 'ssl', 'crypto', 'z', 'pthread', 'gdi32', 'ws2_32']
        if platform() == 'Windows'
        else
        # UNIX
        ['python2.7', 'ssh2', 'ssl', 'crypto', 'z', 'pthread']
    ),
    extra_compile_args = ['-O3', '-flto'] + (['-mwin32'] if platform() == 'Windows' else []),
    extra_link_args = ['-O3', '-flto']
)


setup(
    name = "Threaded remote manager",
    version = '0.91',
    description = 'UIMT threaded remote manager implemented in ANSI C',
    author = 'Vadym Yusanenko',
    author_email = 'usanenko.vadim@gmail.com',
    url = 'https://github.com/yusanenko-vadim/ThreadedRemoteSSHManager',
    ext_modules=[extension_mod]
)
