# vm_mem_dump_tool

Usage:
1. Install Guest OS Windows 7 in VirtualBox.
2. Install python in the guest OS.
3. Copy guest_script.py and files/ to C:\ in the guest OS.
4. Make the guest OS autorun "python guest_script.py" when it starts up.
5. Make a snapshot named "snapshot" when the guest OS starts but before it runs guest_script.py.
5. Set your FILES_PATH and DUMP_PATH in the host_script.py.
6. Run "python host_script.py" on the host OS.
