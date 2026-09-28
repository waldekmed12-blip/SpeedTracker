[app]
title = SpeedTracker
package.name = speedtracker
package.domain = org.speedtracker
source.dir = SpeedTracker
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyttsx3,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# Dodane linijki rozwiązujące problem z licencjami:
android.accept_sdk_license = True
android.api = 33
android.min_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
