# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

import time

# CUSTOM IMPORTS =========================================================
# from LIBRARIES import spotify_api as sa
# from LIBRARIES import spotify_utils as su

# ========================================================================
# MAIN 
# ========================================================================

def main():
	section("START")
	print("hi")
	section("END")

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n{x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# END
# ========================================================================

main()