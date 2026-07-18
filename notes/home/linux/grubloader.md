
# When dropping into UEFI shell
# The EFI boot entry wasn't created properly during installation. Boot manually from the shell:

FS0:
cd EFI\ubuntu
grubx64.efi


# Fixing the boot entry so it doesn't drop to UEFI shell on next reboot:

sudo grub-install /dev/sda
sudo update-grub

Installing for x86_64-efi platform.
Installation finished. No error reported.
Sourcing file `/etc/default/grub'
Sourcing file `/etc/default/grub.d/init-select.cfg'
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-5.15.0-171-generic
Found initrd image: /boot/initrd.img-5.15.0-171-generic
Warning: os-prober will not be executed to detect other bootable partitions.
Systems on them will not be added to the GRUB boot configuration.
Check GRUB_DISABLE_OS_PROBER documentation entry.
Adding boot menu entry for UEFI Firmware Settings ...
done


# Now check disc again

lsblk
df -h


