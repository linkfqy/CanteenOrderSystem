@echo off
pyside6-rcc resources.qrc -o resources_rc.py
pyside6-uic -o ./modules/ui_main.py ./modules/main.ui 