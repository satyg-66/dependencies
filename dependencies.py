#!/usr/bin/env python3

# AUTHOR: Jonas Ingemarsson
# GITHUB: https://github.com/satyg-66
# DESC: Automatic installation of dependencies needed for my config
# WARNING: This script is for testing purpose only. It may have flaws, and may not fit your config.
#          I do not take any responsible for any damage this script may cause.

import os

pacman_dependencies = ["fish", "xmonad", "xmonad-contrib", "xmobar", "firefox", "termite", "alacritty", "pcmanfm", "nitrogen", "picom", "emacs", "exa", "ttf-jetbrains-mono", "adobe-source-code-pro-fonts", "awesome-terminal-fonts"]
yay_dependencies = ["nerd-fonts-mononoki"]
git_dependencies = ["https://github.com/satyg-66/dotfiles.git", "https://git.suckless.org/dmenu", "https://github.com/hlissner/doom-emacs ~/.emacs.d"]

def install_dependencies(pacman_dependencies, yay_dependencies, git_dependencies):
    pacman = "sudo pacman -S "
    yay = "yay -S "
    git = "git clone "
    all_pacman = pacman + " ".join(pacman_dependencies)
    all_yay = yay + " ".join(yay_dependencies)

    try:
        os.system(all_yay)
        os.system(all_pacman)
        for dependencie in git_dependencies:
            git_clone = git + dependencie
            os.system(git_clone)
    except:
        quit("Something went wrong during the installation... program terminated!")
    postinstall()

def postinstall():
    try:

        os.system("sudo mv ~/dependencies/dmenu /usr/local/dmenu && cd /usr/local/dmenu && sudo make clean install && cd ~")
        os.system("cat ~/dependencies/config >> ~/.bashrc && source ~/.bashrc")
        os.system("~/.emacs.d/bin/doom install")
        os.system("mkdir ~/.xmonad ~/.config/xmobar")
        os.system("mv ~/dependencies/dotfiles/termite/config ~/.config/termite/")
        os.system("mv ~/dependencies/dotfiles/xmonad.hs ~/.xmonad/")
        os.system("mv ~/dependencies/dotfiles/doom.d/* ~/.doom.d/")
        os.system("mv ~/dependencies/dotfiles/xmobarrc ~/.config/xmobar/")
        os.system("chsh -s $(which fish)")
        os.system("mv ~/dependencies/dotfiles/fish/config.fish ~/.config/fish/")
        os.system("rm -rf ~/dependencies")
    except:
        quit("Something went wrong during the post installation... program terminated!")

def main():
    print("[+] Installing dependencies needed for Xmonad, Doom-Emacs, xmobar and such.")
    os.system("sleep 2")
    install_dependencies(pacman_dependencies, yay_dependencies, git_dependencies)

if __name__ == "__main__":
    main()
