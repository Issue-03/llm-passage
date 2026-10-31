# Testing for `embrouter/` 

This directory 1:1 maps the the `embrouter/` directory, and can only contain mocked tests. 

The point of this is to:
1. Increase test coverage of `embrouter/`
2. Make it easy for contributors to add tests for the `embrouter/` package and easily run tests without needing LLM API keys. 


## File name conventions

- `embrouter/proxy/test_caching_routes.py` maps to `embrouter/proxy/caching_routes.py`
- `test_<filename>.py` maps to `embrouter/<filename>.py`











