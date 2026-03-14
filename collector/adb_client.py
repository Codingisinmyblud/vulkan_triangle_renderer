import subprocess

def run_adb(cmd):
    try:
        result = subprocess.run(["adb"] + cmd.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return ""
