#!/usr/bin/env bash
set -e
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc
Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1
fluxbox & 
x11vnc -display :1 -nopw -forever -shared -rfbport 5902 &
websockify --web=/usr/share/novnc 6082 localhost:5902 &
