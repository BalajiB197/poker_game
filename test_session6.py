import os
import session6
from session6 import *
import pytest


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"