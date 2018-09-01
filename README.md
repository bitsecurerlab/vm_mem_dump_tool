# vm_mem_dump_tool

Usage:
1. Install Guest OS Windows 7 in VirtualBox, install the applications in files/app.txt, and install python in the guest OS.
2. Copy guest_script.py and files/ to C:\ in the guest OS.
3. Make the guest OS autorun "python guest_script.py" when it starts up.
4. Creat a snapshot named "snapshot" in VirtualBox when the guest OS starts but before it runs guest_script.py.
5. Set your FILES_PATH and DUMP_PATH in the host_script.py.
6. Run "python host_script.py" in the host OS.
