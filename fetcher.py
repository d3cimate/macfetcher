# 

import os
import platform
import socket
import subprocess

inf = platform.uname()

# def get_uptime():
#     up = subprocess.run(['uptime'], capture_output=True)
#     stdout = up.stdout.decode('ascii')
#     for line in stdout.splitlines():
#         if 'up' in line:
#             return line[line.rfind('up') + 4:line.rfind(', ')] # fix this

def getuptime():
    up = os.popen('uptime').read()[11:15] # make this better
    return up

# def getup():
#     up = float(os.popen("sysctl -n kern.boottime").read()[8:18])
#     hrs = up / 3600
#     min = (hrs - int(hrs)) * 60
#     hrs = int(hrs)
#     min = int(min)
#     string = ''
#     if hrs != 0 and min != 0:
#         string += str(hrs) + ' hours and '
#         string += str(min) + ' minutes'
#     elif min != 0 or hrs == 0:
#         string += str(min) + ' minutes'
#     elif hrs!=0 and min == 0:
#         string += str(hrs) + ' hours'
#     return string
#     return up

uptime = getuptime()

def get_packages():
    with os.popen("brew list | wc -l") as brew:
        return brew.read().strip() + " (brew)"

packages = get_packages()

def get_shell():
    shell_type = os.environ['SHELL']
    if shell_type == "/usr/bin/zsh" or shell_type == "/bin/zsh":
        return "zsh"
    elif shell_type == "/usr/bin/fish" or shell_type == "/bin/fish":
        return "fish"
    elif shell_type == "/usr/bin/bash" or shell_type == "/bin/bash":
        return "bash"

shell = get_shell()

def get_term():
    term_type = os.environ['TERM_PROGRAM']
    if term_type == "iTerm.app":
        return "iTerm2"
    elif term_type == 'Apple_Terminal':
        return "Apple Terminal"
    else:
        return term_type

term = get_term()

def get_model():
    with os.popen("sysctl -n hw.model") as macmodel:
        with os.popen("kextstat | grep -F -e 'FakeSMC' -e 'VirtualSMC'") as hackintosh:
            if hackintosh != 0:
                return "Hackintosh (SMBIOS: " + macmodel.read().strip() + ")"
            else:
                return macmodel.read().strip()

model = get_model()

def get_cpu():
    with os.popen("sysctl -n machdep.cpu.brand_string") as cpu:
        return cpu.read().strip()

cpu = get_cpu()

def get_os():
    with os.popen("sw_vers | xargs | awk '{print $2, $4, $6}'") as opsys:
        return opsys.read().strip() + " " + inf.machine

ver = get_os()

def get_username():
    with os.popen("whoami") as username:
        return username.read().strip()

username = get_username()

# def get_gpu():
#     gpu = subprocess.run(['system_profiler', 'SPDisplaysDataType', "|", "grep", "'Chipset Model'"], capture_output=True)
#     stdout = gpu.stdout.decode('ascii')
#     for line in stdout.splitlines():
#         if 'Chipset Model:' in line:
#             chipset = line.split('Chipset Model: ')[1]
#     return chipset

def get_gpu():
    with os.popen("system_profiler SPDisplaysDataType | grep 'Chipset' | awk '{print $3, $4, $5, $6}'") as gpu:
        return gpu.read().strip()
    
gpu = get_gpu()

# def get_resolution():
#     resolution = subprocess.run(['system_profiler', 'SPDisplaysDataType', "|", "grep", "'UI Looks like'"], capture_output=True)
#     stdout = resolution.stdout.decode('ascii')
#     for line in stdout.splitlines():
#         if 'UI Looks like:' in line:
#             res = line.split('UI Looks like: ')[1]
#     return res

def get_resolution():
    with os.popen("system_profiler SPDisplaysDataType | grep UI | xargs | awk '{print $4, $5, $6, $7, $8}'") as resolution:
        return resolution.read().strip()
    
res = get_resolution()

print("  ","  ", f"\033[37;1m{username}@\033[36;1m{inf.node}\033[m")
# check length of ^ and adjust v accordingly
print("  ","  ", f"\033[37;1m--------------------------------\033[m")
print("  ","  ", f"\033[37;1m• OS:            \033[36;1m{ver}\033[m")
print("  ","  ", f"\033[37;1m• Host:          \033[36;1m{model}\033[m")
print("  ","  ", f"\033[37;1m• Kernel:        \033[36;1m{inf.system} {inf.release}\033[m")
print("  ","  ", f"\033[37;1m• Uptime:        \033[36;1m{uptime}\033[m")
print("  ","  ", f"\033[37;1m• Packages:      \033[36;1m{packages}\033[m")
print("  ","  ", f"\033[37;1m• Shell:         \033[36;1m{shell}\033[m")
print("  ","  ", f"\033[37;1m• Resolution:    \033[36;1m{res}\033[m")
print("  ","  ", f"\033[37;1m• DE:            \033[36;1mAqua\033[m")
print("  ","  ", f"\033[37;1m• WM:            \033[36;1mQuartz Compositor\033[m")
# print("  ","  ", f"\033[37;1m• WM Theme:      \033[36;1mQuartz Compositor\033[m")
print("  ","  ", f"\033[37;1m• Terminal:      \033[36;1m{term}\033[m")
# print("  ","  ", f"\033[37;1m• Terminal Font: \033[36;1m{inf.release}\033[m")
print("  ","  ", f"\033[37;1m• CPU:           \033[36;1m{cpu}\033[m")
print("  ","  ", f"\033[37;1m• GPU:           \033[36;1m{gpu}\033[m")
# print("  ","  ", f"\033[37;1m• Memory:        \033[36;1m{cpu}\033[m")

# TBA: 
# 1. Above comments
# 2. Public and Private IP
# 3. Battery (retrieve percentage and status)
# 4. Fix uptime
# 5. Properly retrieve WM