"""
EmbRouter Search API module.
"""

from embrouter.search.cost_calculator import search_provider_cost_per_query
from embrouter.search.main import asearch, search

__all__ = ["asearch", "search", "search_provider_cost_per_query"]
