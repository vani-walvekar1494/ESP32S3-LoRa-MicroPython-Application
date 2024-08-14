import network
import time
import socket
import _thread

# Replace with your Wi-Fi credentials
ssid = 'MikroTik-D47CBA'
password = '12345678'

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    wlan.active(True)  # Activate the interface
    wlan.connect(ssid, password)  # Connect to Wi-Fi

    max_attempts = 10
    attempt = 0

    # Wait for the connection to establish
    while attempt < max_attempts and not wlan.isconnected():
        print('Attempting to connect...')
        attempt += 1
        time.sleep(1)

    if wlan.isconnected():
        print('Connected to Wi-Fi')
        print('Network configuration:', wlan.ifconfig())
    else:
        print('Failed to connect to Wi-Fi')

def log_message(message):
    max_file_size = 1024 * 1024  # 1 MB file size limit
    log_file_path = '/lora_logs.txt'
    
    # Open the log file in append mode
    with open(log_file_path, 'a') as log_file:
        # Check file size and discard old content if necessary
        if log_file.tell() >= max_file_size:
            # Truncate the file to 0 bytes
            log_file.truncate(0)
            log_file.seek(0)
        
        # Write the message to the log file
        log_file.write(message + '\n')

def start_web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        try:
            cl, addr = s.accept()
            print('Client connected from', addr)
            cl_file = cl.makefile('rwb', 0)
            while True:
                line = cl_file.readline()
                if not line or line == b'\r\n':
                    break
            
            # Read the log file
            log_file_path = '/lora_logs.txt'
            with open(log_file_path, 'r') as log_file:
                log_data = log_file.read()
            
            # Simple response with the log data
            response = """\
HTTP/1.1 200 OK
Content-Type: text/plain

{}
""".format(log_data)
            cl.send(response)
            cl.close()
        except OSError as e:
            print("Error in server:", e)

# Connect to Wi-Fi
connect_to_wifi()

# Start the web server in a separate thread
_thread.start_new_thread(start_web_server, ())

while True:
    time.sleep(10)  # Main loop doing nothing, just keeping the device running
