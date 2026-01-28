# Remount /boot if it's umbrel os
if [ -d "/home/umbrel/umbrel" ]; then
    if [ "$(mount | grep '/boot' | awk '{print $4}')" = "ro" ]; then
        echo "Remount /boot as read-write..."
        mount -o remount,rw /boot
    else
        echo "/boot is already mounted as read-write."
    fi
else
    echo "Not Umbrel OS, skip remount /boot."
    exit 0
fi
