import subprocess
import os

ip_index = os.environ.get("ORBIT_IP_INDEX")
ip_name = os.environ.get("ORBIT_IP_NAME")
ip_version = os.environ.get("ORBIT_IP") 

# Add untracked files
child = subprocess.Popen(['git', 'add', ip_index])
rc = child.wait()
if rc != 0:
    exit(rc)
# Commit the changes
child = subprocess.Popen(['git', 'commit', '-m', "Publishes "+ip_name+':'+ip_version])
rc = child.wait()
if rc != 0:
    exit(rc)
# Push the changes to the remote
child = subprocess.Popen(['git', 'push'])
rc = child.wait()
if rc != 0:
    exit(rc)

