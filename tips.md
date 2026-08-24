
## Pre setup

    alias k=kubectl                         # will already be pre-configured
    export do="--dry-run=client -o yaml"    # k get pod x $do
    export now="--force --grace-period 0"   # k delete pod x $now

###Vim
To make vim use 2 spaces for a tab edit ~/.vimrc to contain:

    set tabstop=2
    set expandtab
    set shiftwidth=2
