import sys
import os

# Get the absolute path of the directory containing this file
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)

# Add the directory named "my_module" to the Python path
print(parent_dir)
sys.path.append(os.path.join(parent_dir))

import pytest
import requests
from api.config import STAR_WARS_BASE_URL

@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


@pytest.fixture(scope="session")
def base_url():
    return STAR_WARS_BASE_URL