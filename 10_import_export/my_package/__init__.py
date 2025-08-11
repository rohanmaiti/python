# my_package/__init__.py
PACKAGE_VERSION = "1.0.0"
DEBUG_MODE = False

def initialize_logging():
    # Some setup code for logging
    print("Logging initialized for my_package!")

initialize_logging() # This function will run when the package is imported

#* Controlling What’s Visible with __all__
"""
The __all__ variable is a special list defined within __init__.py (or any module) that controls 
what names are exported when a client uses from package_name import * (a "wildcard import"). 
This is a powerful mechanism for explicitly defining the public interface of your package.
"""

from .math_utils import add, _internal_helper
__all__=["add"] # Only 'add' will be imported with '*'