# ✅ Option 1: Import whole module
# from utils import math_utils
# print(math_utils.PI)

# ✅ Option 2: Import specific functions/variables (like JS destructuring)
from utils.math_utils import add, PI
print(PI)

# ✅ Option 3: Import with alias
from utils import math_utils as mu
print(mu.PI)


# ✨ 3. Wildcard Import (⚠️ Not recommended)
from math_utils import *
print(add(2, 3))  #