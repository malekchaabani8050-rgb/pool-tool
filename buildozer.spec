[app]

# (str) Title of your application
title = Pool Guideline Tool

# (str) Package name
package.name = pooltool

# (str) Package domain
package.domain = org.helper

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Crucial: This tells GitHub to include Kivy
requirements = python3,kivy

# (list) Supported orientations
# Set to landscape for 8 Ball Pool
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# SYSTEM_ALERT_WINDOW is the "Display over other apps" permission
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
