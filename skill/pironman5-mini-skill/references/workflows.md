# Pironman 5 Mini – Working Notes

## 1. Bring-up checklist
1. Update firmware (`sudo rpi-eeprom-update -a`) while the board is still exposed.
2. Pre-test camera or other flex cables before routing them through the tight Mini chassis.
3. Install the Pironman daemon (`sudo pip install pironman5` or vendor script) and verify `pironman5 -c` succeeds before closing the panels.
4. Confirm your HDMI cables terminate in *micro* HDMI; adapters are easy to forget once the Pi is sealed inside.

## 2. Service health
```bash
systemctl status pironman5.service
journalctl -u pironman5.service -n 100 --no-pager
sudo tail -f /var/log/pironman5/pm_auto.rgb.log
```
- Restart after CLI changes: `sudo systemctl restart pironman5.service`.
- With no OLED, rely on the dashboard (`http://<pi-ip>:34001`) or `pironman5 -c` for telemetry.

## 3. CLI focus areas
| Task | Command |
| --- | --- |
| Enable RGB (fan + strip) | `sudo pironman5 -re true` |
| Pick solid color | `sudo pironman5 -rs solid && sudo pironman5 -rc 33a1ff` |
| Breathe effect | `sudo pironman5 -rs breathing && sudo pironman5 -rb 40` |
| Adjust LED count (fan blades count as segments) | `sudo pironman5 -rl 5` (default) |
| Dashboard launch | `pironman5 launch-browser` |
| Config dump | `pironman5 -c` |

## 4. Cooling + acoustics
- The active cooler behaves like the official Pi 5 fan; its curve is configured in the dashboard under **Performance → Fan Curve**.
- For silent builds, lower `rgb_brightness` and cap fan RPM using the dashboard; the Mini has less mass to absorb vibration.

## 5. Storage workflow
1. Shut down, install NVMe, secure with the short standoff (long standoffs collide with the lid).
2. Boot and verify `dmesg | grep nvme` to confirm the link.
3. Format: `sudo mkfs.ext4 /dev/nvme0n1` or build Btrfs/RAID arrays on external drives if you need redundancy (Mini has only one internal slot).

## 6. Integrating with OpenClaw automations
- Grant the OpenClaw user access to `gpio`, `i2c`, and `dialout` groups so CLI calls succeed.
- Because there is no OLED, plan on pushing telemetry to the dashboard or chat messages (fan speed, temperature, storage usage).
- Keep helper scripts (e.g., `~/bin/pi-mini-led.sh`) for repeated LED modes to minimize mistakes on the cramped hardware.

## 7. Troubleshooting quick hits
- **RGB dark:** Check `"rgb_enable": false` in `pironman5 -c`; re-enable and restart.
- **High temps:** Verify the side RGB fan spins—if not, reseat its JST connector and retighten the acrylic panel.
- **Micro HDMI loose:** Replace adapters with locking cables; the Mini case tugs on connectors when you route them downward.
