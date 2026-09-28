[app]
title = SpeedTracker
package.name = speedtracker
package.domain = org.speedtracker

# Tutaj wskazujemy podkatalog z kodem aplikacji:
source.dir = SpeedTracker

source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyttsx3,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

[buildozer]
log_level = 2
warn_on_root = 1
