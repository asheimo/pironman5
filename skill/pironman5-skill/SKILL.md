---
name: pironman5
description: Operate and customize the SunFounder Pironman 5 enclosure (single NVMe, RGB, OLED, fans, dashboard, service, IR). Use when issuing `pironman5` CLI commands, editing `/opt/pironman5/config.json`, working with its displays, LEDs, fans, IR receiver, or citing hardware capabilities/specs from the official docs.
---

# Pironman 5 Skill

Use this skill whenever a task touches the SunFounder Pironman 5 case, its bundled services, or hardware add-ons.

## References
- Hardware overview & specifications: [`references/features.md`](references/features.md)
- Full CLI syntax & examples: [`references/cli-cheatsheet.md`](references/cli-cheatsheet.md)
- Source manual: <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5/intro_pironman5.html>

## Quick Start Workflow

1. **Install the software** (if not already done):
   ```bash
   curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash
   ```
   Select **1) Pironman 5** when prompted. Reboot when finished.

   > For PiPower 5 users: `curl -sSL "..." | sudo bash -s -- --pipower5`

2. **Verify service health**: `systemctl status pironman5.service`
3. **Tail logs** for a specific addon (e.g., OLED): `journalctl -u pironman5.service -f` or `cat /var/log/pironman5/pironman5.log`
4. **Inspect/adjust config**: `sudo pironman5 -c` or edit `/opt/pironman5/config.json`
5. **Apply changes**: Always `sudo systemctl restart pironman5.service` after any CLI or config update.
6. **Validate hardware response** (RGB glow, OLED page, fan spin, etc.)
7. **Document deviations** (custom OLED pages, added LED strips, changed fan pins) for future-you.

## Common Operations

### RGB Lighting (4× WS2812-5050)
- Enable/disable, color, brightness, mode, speed, and LED count via the `-re/-rc/-rb/-rs/-rp/-rl` flags.
- Built-in modes: `solid`, `breathing`, `flow`, `flow_reverse`, `rainbow`, `rainbow_reverse`, `hue_cycle`.
- Rainbow/hue-cycle modes override manual color settings.
- External WS2812 strips can be chained via the RGB OUT pins — update the LED count with `-rl` to match.

### OLED Display (0.96" 128×64 I2C @0x3C)
- `-oe` toggles power, `-or` sets 0°/180° rotation, `-op` lists active pages (e.g., `mix,performance,ips,disk`), `-os` sets sleep timeout (0 = never).
- **Wake behavior (v1.3.6+)**: OLED wake-up uses the power button. Remove the vibration switch jumper to avoid GPIO conflicts.
- **Pre-v1.3.6**: Vibration switch (onboard) wakes the OLED.
- Troubleshoot: check FPC cable → verify I2C (`i2cdetect -y 1` → should see `0x3C`) → inspect logs.

### Dashboard
- Accessible at `http://<device-ip>:34001`.
- Required for Home Assistant images (CLI control limited there).
- `pironman5 launch-browser` auto-opens the UI if the package is present.
- `-rd` removes dashboard components.
- Use `--disable-dashboard` flag during install to skip the dashboard.

### Power Button
- **Single press**: Power on / wake OLED / switch OLED page forward.
- **Double press**: Switch OLED page backward.
- **Hold 2 sec**: Safe shutdown (requires "Full Power Off" set in `raspi-config` → Advanced Options → A12 Shutdown Behaviour).
- **Hold 5 sec**: Force hard shutdown.

### GPIO Fans (2× 40×40×10mm)
- Both fans share a single control pin (default GPIO6) and are controlled together.
- Fan modes: `0` Always On, `1` Performance (50°C), `2` Cool (60°C), `3` Balanced (67.5°C), `4` Quiet (70°C).
- Change control pin: `-gp <pin>`.

### CPU Fan (Tower Cooler, 4-pin PWM)
- Controlled by the Raspberry Pi 5 firmware, not the `pironman5` service.
- Default fan curve (automatic): < 50°C off, 50°C+ 30%, 60°C+ 50%, 67.5°C+ 70%, 75°C+ 100%.
- Manual override: `pinctrl FAN_PWM op dl` (on), `pinctrl FAN_PWM op dh` (off), `pinctrl FAN_PWM a0` (auto).
- Customize thresholds via `/boot/firmware/config.txt` → `dtparam=fan_temp0=...`
- Verify temperature: `vcgencmd measure_temp`

### Infrared Receiver
- Model: IRM-56384, 38 kHz, connected to GPIO13.
- Install `lirc`: `sudo apt-get install lirc -y`
- Raw capture: `mode2 -d /dev/lirc0`
- Map buttons in `/etc/lirc/lircd.conf`
- Disable by removing the J8 jumper cap to free GPIO13.

### Single NVMe & AI Expansion
- One M.2 M-key slot (2230/2242/2260/2280) connected directly to the Pi 5's PCIe Gen2 x1 lane.
- Supports NVMe SSDs or a Hailo-8/8L AI accelerator (one at a time).
- **Power warning**: Use a quality 27W USB-C supply, especially with power-hungry NVMe drives.
- **Not compatible** with Raspberry Pi AI HAT+ — use the separate Hailo module directly in the M.2 slot.

### Service & Config
- Service subcommands: `pironman5 start|stop|launch-browser`
- Always restart after config changes: `sudo systemctl restart pironman5.service`
- Data logging: retention (`-drd`), history enable (`-eh`), debug level (`-dl`), temp unit (`-u`).

## Hardware & Expansion Checklist

Consult `references/features.md` for full specs when planning builds:
- **Single NVMe slot uses the Pi 5's direct PCIe Gen2 lane** — choose between storage or AI, not both simultaneously.
- **Power matters**: A clean 27W USB-C supply is strongly recommended, especially with NVMe drives or AI cards.
- **RGB expansion**: 4 onboard WS2812 LEDs. Chain external strips via RGB OUT — update LED count with `-rl`.
- **GPIO awareness**: IR receiver (GPIO13), RGB (GPIO10/SPI), GPIO fan (GPIO6), OLED (I2C SDA/SCL) — remove jumpers to free pins for other uses.
- **RTC**: 1220 battery for real-time clock.
- **Spring-loaded microSD slot**: Easy card access without tools.

## Troubleshooting Tips

### OLED Blank or Garbage Display
- Ensure FPC cable is fully seated; reseat and reboot.
- Check I2C: `i2cdetect -y 1` should show `0x3C`.
- Enable I2C: add `dtparam=i2c_arm=on` to `/boot/firmware/config.txt`.
- Inspect logs: `cat /var/log/pironman5/pironman5.log`
- Restart service: `sudo systemctl restart pironman5.service`

### RGB Unresponsive
- Verify RGB jumper on IO board (J9 area, connects GPIO10) is installed.
- Enable SPI: `sudo raspi-config` → `3 Interfacing Options` → `I3 SPI` → `YES`, then reboot.
- Ensure `rgb_enable` is `true` in config.
- Restart service.

### GPIO Fans Not Spinning
- Check FAN jumper caps (J4/J5 area) are installed on the IO board.
- Test: `sudo pironman5 -gm 0` (Always On mode).
- Direct test: connect fan to 5V/GND on Pi GPIO.
- Check logs in Dashboard or `/var/log/pironman5/pironman5.log`.

### CPU Fan Not Spinning
- Check the 4-pin PWM cable is connected to the Pi 5's CPU fan header.
- Check current temp: `vcgencmd measure_temp` — fan starts ~50°C by default.
- Manual override: `pinctrl FAN_PWM op dl`
- If completely dead, check the FAQ for custom fan curve config.

### Dashboard Shows No Data
- Clear browser cache / use incognito mode.
- Verify services: `sudo systemctl status pironman5` and `sudo systemctl status influxdb`.
- Check database: `influx` → `SHOW DATABASES;` — should see `pironman5`.
- Use Dashboard "Settings → Clear All Data" if corrupted.
- Reinstall as last resort.

### NVMe Not Detected
- Verify SSD is fully seated in the M.2 slot.
- Check FFC/FPC cable connection from the PCIe breakout to the Pi 5.
- List PCIe devices: `lspci | grep -i nvme` or `lspci | grep -i "Non-Volatile"`
- Check dmesg: `dmesg | grep -i nvme`
- Try forcing PCIe to Gen2: add `dtparam=pciex1_gen=2` to `/boot/firmware/config.txt`.
- Ensure adequate power — brownouts cause NVMe dropouts.

### Power / Boot Issues
- Random reboots → check power supply (needs 27W / 5V 5A).
- Red LED, no boot → reseat USB-HDMI adapter, test Pi 5 outside the case, or restore bootloader.
- For "Full Power Off" on shutdown: `sudo raspi-config` → Advanced Options → A12 Shutdown Behaviour → B1 Full Power Off.

## Workflow Pointers
- Script repeatable tasks (e.g., custom OLED page installers) separately; keep this skill focused on vendor-supported controls.
- When modifying packaged Python code under `/opt/pironman5/venv/`, document changes so future updates don't silently overwrite them.
- When asked "what can Pironman 5 do," lead with the headline features from `references/features.md` and tie them to actionable controls.
