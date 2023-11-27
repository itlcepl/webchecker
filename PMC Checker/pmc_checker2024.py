import requests
import tkinter as tk
import winsound
import threading
import time

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"The website {url} is up and running!"
        else:
            return f"The website {url} is down with status code {response.status_code}"
    except requests.ConnectionError:
        for i in range(0,100):
            winsound.Beep(1000, 1500)
        time.sleep(60)
        return f"Failed to connect to {url}"

def continuous_check():
    while True:
        website_url = entry.get()
        status = check_website_status(website_url)
        status_label.config(text=status)
        if "down" in status.lower():
           for i in range(0,100):
            winsound.Beep(1000, 1500) # Ring the bell if the website is down
        time.sleep(60)  # Check every 10 seconds (adjust as needed)

def start_continuous_check():
    check_thread = threading.Thread(target=continuous_check)
    check_thread.daemon = True
    check_thread.start()

root = tk.Tk()
root.title("Continuous Website Status Checker")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter website URL:")
label.pack()

entry = tk.Entry(frame, width=40)
entry.pack()

start_button = tk.Button(frame, text="Start Continuous Check", command=start_continuous_check)
start_button.pack(pady=10)

status_label = tk.Label(frame, text="")
status_label.pack()

root.mainloop()