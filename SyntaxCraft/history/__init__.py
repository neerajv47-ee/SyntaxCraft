"""
SyntaxCraft History Package
Local database persistence for code generation logs.
"""

from .history_manager import add_history, get_history, clear_history

__all__ = ["add_history", "get_history", "clear_history"]
