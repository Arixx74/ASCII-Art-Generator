from distutils.core import setup
import py2exe, sys, os

#sys.argv.append('')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "Pyte.py"}],
    zipfile = None,
    )