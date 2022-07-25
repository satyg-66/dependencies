#!/usr/bin/env python3

# AUTHOR: Jonas Ingemarsson
# GITHUB: https://github.com/satyg-66
# DESC: Automatic installation of dependencies needed for my config
# WARNING: This script is for testing purpose only. It may have flaws, and may not fit your config.
#          I do not take any responsible for any damage this script may cause.

import os
import subprocess

pacman_dependencies = ["xmonad", "xmonad-contrib", "firefox", "termite", "alacritty", "pcmanfm", "nitrogen", "picom", "emcas", "exa", "ttf-jetbrains-mono", "adobe-source-code-pro-fonts", "awesome-terminal-fonts"]
yay_dependencies = ["nerd-fonts-mononoki"]
git_dependencies = ["https://git.suckless.org/dmenu", "https://github.com/hlissner/doom-emacs ~/.emacs.d"]

def install_dependencies(pacman_dependencies, yay_dependencies, git_dependencies):
    pacman = "yes | sudo pacman -S "
    yay = "yes | sudo yay -S "
    git = "git clone "
    all_pacman = pacman + " ".join(pacman_dependencies)
    all_yay = yay + " ".join(yay_dependencies)

    try:
        os.system(all_pacman)
        os.system(all_yay)
        for dependencie in git_dependencies:
            git_clone = git + dependencie
            os.system(git_clone)
    except:
        quit("Something went wrong during the installation... program terminated!")
    postinstall()

def postinstall():
    alias = ['"emacsclient -c -a \'emacs\'"']
    try:
        os.system("mv ~/dependencies/dmenu /usr/local/dmenu && cd /usr/local/dmenu && make clean install && cd ~")
        with open("~/dependencies/config", "r") as f:
            data = f.read()
            os.system(f"cat {data} >> ~/.bashrc && source ~/.bashrc")
        os.system("~/.emacs.d/bin/doom install")
        os.system("git clone https://github.com/satyg-66/dotfiles.git ~")
        os.system("mkdir ~/.xmonad && mv ~/dotfiles/xmonad.hs ~/.xmonad/xmonad.hs")
        os.system("mv ~/dotfiles/doom.d/* ~/.doom.d")
        os.system("mv ~/dotfiles/xmobarrc ~/.config/xmobar/xmobarrc")
        os.system("rm -rf ~/dotfiles")
    except:
        quit("Something went wrong during the post installation... program terminated!")

def main():
    print("[+] Installing dependencies needed for Xmonad, Doom-Emacs, xmobar and such.")
    subprocess.run(["sleep", "2"], check=True)
    install_dependencies(pacman_dependencies, yay_dependencies, git_dependencies)

if __name__ == "__main__":
    main()
