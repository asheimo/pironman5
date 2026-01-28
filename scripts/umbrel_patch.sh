# If not umbrel os, skip
if ! [ -d "/home/umbrel/umbrel" ]; then
    echo "Not Umbrel OS, skip remount /boot."
    exit 0
fi

# Remount /boot if it's read-only
if [ "$(mount | grep '/boot' | awk '{print $4}')" = "ro" ]; then
    echo "Remount /boot as read-write..."
    mount -o remount,rw /boot
else
    echo "/boot is already mounted as read-write."
fi

# cp udev rule to /etc/udev/rules.d/
cp ./bin/99-com.rules /etc/udev/rules.d/
# reload udev rules
udevadm control --reload-rules
