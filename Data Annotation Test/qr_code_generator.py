import qrcode

# Example: Instagram handle
url = "https://www.facebook.com/CanonCollegeUK"

# wifi network
wifi_data = "WIFI:T:WPA;S:4ABC Hyperoptic 1Gb Fibre 2.4Ghz;P:auCECjZReHNf;;"

img = qrcode.make(wifi_data)
img.save("wifi_qr.png")