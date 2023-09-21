from datetime import date
import time
""" The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds."""

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

"""  from the iso format yyyy-mm-dd"""
d = date.fromisoformat('2019-11-04')
print(d)
