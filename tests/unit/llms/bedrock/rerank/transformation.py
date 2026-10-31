import json

import pytest
from fastapi.testclient import TestClient

from unittest.mock import MagicMock, patch

from embrouter import rerank
from embrouter.llms.custom_httpx.http_handler import HTTPHandler
