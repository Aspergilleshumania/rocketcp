# testapp/views.py
from django.http import HttpResponse
import subprocess
import os
import datetime
import pytz
import getpass

def htop_view(request):
    try:
        # Execute htop command (without color options)
        htop_process = subprocess.Popen(['htop', '-bn1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        htop_output, htop_err = htop_process.communicate(timeout=10)
        if htop_err:
            htop_output = f"Error running htop: {htop_err}"

        # Execute top command
        top_process = subprocess.Popen(['top', '-bn1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        top_output, top_err = top_process.communicate(timeout=10)
        if top_err:
            top_output = f"Error running top: {top_err}"

    except subprocess.TimeoutExpired:
        htop_output = "htop command timed out."
        top_output = "top command timed out."
    except FileNotFoundError:
        htop_output = "htop command not found."
        top_output = "top command not found."
    except Exception as e:
        htop_output = f"An error occurred running system commands: {e}"
        top_output = f"An error occurred running system commands: {e}"

    # Get username using getpass
    try:
        username = getpass.getuser()
    except:
        username = "unknown"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")

    # Get full name from environment variable (set this in your Codespace!)
    full_name = os.environ.get('FULL_NAME', 'Your Full Name')

    output = f"Name: {full_name}\n"
    output += f"Username: {username}\n"
    output += f"Server Time (IST): {now_ist}\n"
    output += "Top output:\n"
    output += top_output + "\n"
    output += "HTOP output:\n"
    output += htop_output

    return HttpResponse(output, content_type='text/plain')