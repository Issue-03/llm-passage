import importlib_metadata

try:
    version = importlib_metadata.version("embrouter")
except Exception:
    version = "unknown"
