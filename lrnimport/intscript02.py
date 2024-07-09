#!/usr/bin/env python3
import subprocess  ## <-------- changed
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

try:
    result = subprocess.check_output(['ip', 'a'], text=True)
    print(result)
except subprocess.CalledProcessError as e:
    print(f"Error executing ip command: {e}")
    return None
return result
