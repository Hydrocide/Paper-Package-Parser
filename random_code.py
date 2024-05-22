"""
A spot for quick syntax checking and calculations


"""


hashrate_s = 20 #tokens per second

hasrate_hr = hashrate_s * 60 * 60

tokens = 507091

hr = tokens/hasrate_hr

print(hr)
