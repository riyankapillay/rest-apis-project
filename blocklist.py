"""
blocklist.py
    
This file just contains the blocklist of JWT tokens.
It will be imported by the app and logout resource
so that tokens can be added to the blocklist when
the user logs out   - Likely would store blocklist in
a db and not set in actuality 
    
"""

BLOCKLIST = set()