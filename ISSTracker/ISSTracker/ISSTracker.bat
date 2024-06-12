@echo off
@color f
python ISS-Tracker.py

ping 127.0.0.1 -n 30 > nul