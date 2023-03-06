import subprocess

# Run adb command to start camera app
subprocess.run(["adb", "shell", "am", "start", "-a", "android.media.action.IMAGE_CAPTURE"])