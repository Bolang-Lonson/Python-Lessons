from platform import platform, machine, processor, system, version
#   platform(aliased = False, terse = False)
#   aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
#   terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)
print(platform(), '#platform')
print(platform(terse=True))
print(platform(True, True))
###############################################################
# machine() fxn prints out cpu architecture ie
print(machine(), '#machine')
###############################################################
# The processor() function returns a string filled with the real processor name (if possible).

print(processor(), '#processor')
##############################################################
# A function named system() returns the generic OS name as a string.
# The OS version is provided as a string by the version() function.
print(system(), version())
