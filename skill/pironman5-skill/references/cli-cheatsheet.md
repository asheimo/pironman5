# Pironman 5 — CLI Cheatsheet

All commands require `sudo` unless otherwise noted. After changing system settings, restart the service:

```bash
sudo systemctl restart pironman5.service
```

Verify status / logs:
- `systemctl status pironman5.service`
- `journalctl -u pironman5.service -f`
- `cat /var/log/pironman5/pironman5.log`

---

## Config & Info

| Action | Command |
|--------|---------|
| Show config JSON | `sudo pironman5 -c` |
| Show version | `sudo pironman5 -v` |
| Use custom config path | `sudo pironman5 -cp /path/to/config.json` |
| Change debug level | `sudo pironman5 -dl DEBUG\|INFO\|WARNING\|ERROR\|CRITICAL` |
| Change temperature unit | `sudo pironman5 -u C\|F` |

---

## RGB Lighting (4× WS2812-5050 + chained LEDs)

| Action | Command |
|--------|---------|
| Enable/disable | `sudo pironman5 -re true\|false` |
| Solid color (hex without #) | `sudo pironman5 -rc fe1a1a` |
| Brightness 0–100 | `sudo pironman5 -rb 75` |
| Mode | `sudo pironman5 -rs solid\|breathing\|flow\|flow_reverse\|rainbow\|rainbow_reverse\|hue_cycle` |
| Speed 0–100 | `sudo pironman5 -rp 50` |
| LED count (extend chains) | `sudo pironman5 -rl 12` |

> ⚠ Rainbow, rainbow_reverse, and hue_cycle modes override the `-rc` color setting.

---

## OLED (0.96" 128×64 I2C @0x3C)

| Action | Command |
|--------|---------|
| Enable/disable | `sudo pironman5 -oe true\|false` |
| Rotation 0/180 | `sudo pironman5 -or 180` |
| Sleep timeout in seconds (0 = never) | `sudo pironman5 -os 120` |
| Set pages (comma-separated) | `sudo pironman5 -op mix,performance,ips,disk` |

### OLED Troubleshooting
```bash
# Check I2C bus for device 0x3C
i2cdetect -y 1

# Enable I2C if missing
echo "dtparam=i2c_arm=on" | sudo tee -a /boot/firmware/config.txt

# View OLED-specific logs
journalctl -u pironman5.service -f
cat /var/log/pironman5/pironman5.log
```

---

## GPIO Fans (2× 40mm, shared GPIO6)

| Action | Command |
|--------|---------|
| Set fan mode | `sudo pironman5 -gm 0\|1\|2\|3\|4` |
| Change control pin | `sudo pironman5 -gp 18` |

**Fan modes:**
- `0` — Always On
- `1` — Performance (activates at 50 °C)
- `2` — Cool (activates at 60 °C)
- `3` — Balanced (activates at 67.5 °C)
- `4` — Quiet (activates at 70 °C)

---

## CPU Fan (Tower Cooler, 4-pin PWM)

The CPU fan is controlled by the Pi 5 firmware, not the `pironman5` service. Default curve:
- < 50 °C → Off (0%)
- 50 °C+ → Low (30%)
- 60 °C+ → Medium (50%)
- 67.5 °C+ → High (70%)
- 75 °C+ → Full (100%)

```bash
# Check current temperature
vcgencmd measure_temp

# Manual control
pinctrl FAN_PWM op dl    # Enable fan (low active)
pinctrl FAN_PWM op dh    # Disable fan (high active)
pinctrl FAN_PWM a0       # Return to auto mode

# Custom fan curve — edit /boot/firmware/config.txt:
dtparam=cooling_fan=on
dtparam=fan_temp0=40000
dtparam=fan_temp0_hyst=10000
dtparam=fan_temp0_speed=125
# Reboot to apply
```

---

## Infrared Receiver (IRM-56384, 38 kHz, GPIO13)

```bash
# Install LIRC
sudo apt-get install lirc -y

# Test raw reception
mode2 -d /dev/lirc0

# Map buttons in /etc/lirc/lircd.conf
```

---

## Dashboard

| Action | Command |
|--------|---------|
| Web UI | `http://<device-ip>:34001` |
| Open in browser (local) | `pironman5 launch-browser` |
| Remove dashboard | `sudo pironman5 -rd` |
| Disable on install | `cd ~/pironman5 && sudo python3 install.py --disable-dashboard` |

---

## Service Management

```bash
# Start / stop / restart / status
sudo systemctl start pironman5.service
sudo systemctl stop pironman5.service
sudo systemctl restart pironman5.service
sudo systemctl status pironman5.service

# Or using the pironman5 helper
sudo pironman5 start
sudo pironman5 stop
sudo pironman5 launch-browser
```

---

## Telemetry & Data

| Action | Command |
|--------|---------|
| Enable/disable history | `sudo pironman5 -eh true\|false` |
| Retention days | `sudo pironman5 -drd 30` |
| Debug level | `sudo pironman5 -dl DEBUG` |
| Temperature unit | `sudo pironman5 -u C` |

---

## Storage (Single NVMe)

```bash
# Verify NVMe drive detected
ls /dev/nvme*
lspci | grep -i nvme
dmesg | grep -i nvme

# Format as ext4
sudo mkfs.ext4 /dev/nvme0n1

# Mount permanently — add to /etc/fstab:
# /dev/nvme0n1  /mnt/nvme  ext4  defaults,noatime  0  1

# Boot from NVMe — configure Pi 5 EEPROM boot order:
sudo raspi-config
# → Advanced Options → A4 Boot Order → NVMe/USB Boot
```

> ⚠ Unlike the Max and Pro Max, Pironman 5 has a single M.2 slot. You cannot run dual SSDs or SSD + AI accelerator simultaneously.

---

## Initial Setup (First-Time)

```bash
# 1. Configure safe shutdown
sudo raspi-config
# → Advanced Options → A12 Shutdown Behaviour → B1 Full Power Off

# 2. Enable PCIe Gen2 for NVMe
echo "dtparam=pciex1_gen=2" | sudo tee -a /boot/firmware/config.txt

# 3. Install pironman5 module
curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash
# → Select "1) Pironman 5"

# 4. Reboot
sudo reboot

# 5. Verify
sudo systemctl status pironman5.service
```

---

## Uninstall & Reinstall

```bash
cd ~/pironman5
sudo python3 install.py --uninstall
# Reboot, then:
sudo rm -rf ~/pironman5
curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash
```

---

## Hardware Pin Map

| Component | Pi 5 GPIO | Notes |
|-----------|-----------|-------|
| RGB LEDs | GPIO10 (SPI MOSI) | Jumper J9 |
| IR Receiver | GPIO13 | Jumper J8 |
| GPIO Fan | GPIO6 | Jumper-controlled |
| OLED | I2C SDA/SCL | Address 0x3C |
| CPU Fan | 4-pin PWM header | Firmware-controlled |

Remove jumpers to free pins for alternate use.
