# Simple rule:

adduser → use on Debian/Ubuntu when creating users manually
useradd → use in scripts where you need full control
usermod → use when modifying existing users

# Creates user, NO home dir, NO password, NO shell

useradd milo

# Need to specify everything manually

useradd -m -s /bin/bash milo

# Asks for password, creates home dir, sets shell automatically

adduser milo

# DANGEROUS - removes from all other groups!

usermod -G docker milo

# SAFE - only adds docker, keeps everything else

usermod -aG docker milo

# Usermod — modifies an existing user. It never creates users, only changes their properties:

usermod -aG sudo milo        # add to group (-a = append, -G = groups)
usermod -aG docker,wireshark milo  # add to multiple groups at once
usermod -l newname milo      # rename user
usermod -d /new/home milo    # change home directory
usermod -s /bin/zsh milo     # change default shell
usermod -L milo              # lock account (disable login)
usermod -U milo              # unlock account
