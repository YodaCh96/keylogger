import psutil

PROCNAME = "pythonw.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()