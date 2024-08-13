import subprocess
import os

chan_index = os.environ.get("ORBIT_CHAN_INDEX")
ip_name = os.environ.get("ORBIT_IP_NAME")
ip_version = os.environ.get("ORBIT_IP_VERSION") 

# Add untracked files
child = subprocess.Popen(['git', 'add', chan_index])
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

