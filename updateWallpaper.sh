#!/usr/bin/env bash
sleep 1

WALLPAPER_DIR="$HOME/.config/Wallpapers/"

WALLPAPER=$(find "$WALLPAPER_DIR" -type f -name "*.jpg" | shuf -n 1)

hyprctl hyprpaper preload "$WALLPAPER"
hyprctl hyprpaper wallpaper "eDP-1,$WALLPAPER"


sleep 1

hyprctl hyprpaper unload unused
