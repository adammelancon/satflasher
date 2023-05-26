
# NTP server configuration
ntp_server = "pool.ntp.org"  # NTP server address

def synchronize_time():
    ''' Connects to NTP server and sets pi pico rtc'''
    ntptime.host = ntp_server
    try:
        ntptime.settime()
        print("Time synchronized with NTP server.")
    except OSError as e:
        print("Failed to synchronize time with NTP server:", e)