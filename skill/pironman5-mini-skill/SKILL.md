---
name: pironman5-mini
description: Guide Raspberry Pi 5 builds that live inside the SunFounder Pironman 5 Mini enclosure. Use this skill for assembly notes, cooling/RGB control, NVMe provisioning, pironman5 CLI/dashboard operations, and OpenClaw automations that target the compact Mini case.
---

# SunFounder Pironman 5 Mini

## Quick start
1. Read `references/features.md` to recall the Mini’s constraints (micro HDMI, no OLED, single RGB fan, limited space).
2. Confirm `pironman5.service` is running and capture the current config with `pironman5 -c` before editing anything.
3. Apply LED/fan changes via CLI, then restart the service so OpenClaw tasks inherit the new state.
4. Keep the 27 W PSU connected—the smaller chassis is even less tolerant of voltage dips.

## Core workflows
### 1. Assembly + cable routing
- Dry-fit the GPIO extender and HDMI adapters before tightening the side panels; there is very little slack once the case is closed.
- Route camera or SDR coax along the rear corner to avoid the side fan blades.

### 2. OS, services, and OpenClaw
- Flash Raspberry Pi OS, enable PCIe Gen 2, and install the Pironman stack (`pironman5` CLI + dashboard) before onboarding OpenClaw.
- Add the OpenClaw user to `gpio`, `i2c`, `dialout` so scripted LED controls do not fail.

### 3. Cooling + RGB control
- Mini has no OLED—monitor temps via dashboard or CLI output.
- RGB control: `pironman5 -re true`, set mode (`-rs solid/breathing/...`), color (`-rc <hex>`), brightness (`-rb <0-100>`), LED count (`-rl 5` by default).
- Fan curve lives under the dashboard’s **Performance** tab. For unattended nodes, keep the curve aggressive; the small heatsink saturates fast.

### 4. Storage
- Power down before installing an NVMe drive. Use the short standoff to avoid pressing against the lid.
- After boot, verify `ls /dev/nvme*`, then partition/format with your preferred filesystem.
- External drives can hang off USB 3 if you need redundancy the single internal slot can’t provide.

### 5. Dashboard + scripting
- Dashboard URL: `http://<pi-ip>:34001`. Use it for fan curves, RGB previews, and log review when the CLI is busy.
- For repeated routines (e.g., switching demo colors), keep helper scripts in `~/bin` and call them from OpenClaw automations.

## Diagnostics
- Check logs via `journalctl -u pironman5.service -n 200` and `/var/log/pironman5/pm_auto.rgb.log` for LED/fan issues.
- If the RGB fan stalls, reseat its JST cable and confirm `rgb_enable` is still `true`.

## References
- [`references/features.md`](references/features.md) — Mini-specific hardware summary and selection guidance.
- [`references/workflows.md`](references/workflows.md) — bring-up checklist, CLI table, cooling/storage notes, troubleshooting tips.
