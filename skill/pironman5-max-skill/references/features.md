# Pironman 5 Max — Hardware Highlights

## Chassis & Dimensions
- **Size**: 111.9 × 78.5 × 117 mm (with tower cooler)
- **Material**: Dark anodized aluminum alloy main body + dark acrylic side panels
- **Weight**: Premium build with spring-loaded microSD slot (tool-free access)
- **Support Platform**: Raspberry Pi 5 only

## Power
- USB-C 5 V/5 A input
- 27 W official or SunFounder 27 W PD supply **strongly recommended**, especially when both NVMe slots are populated
- Retro-style metal power button with safe shutdown integration

## Cooling System
| Component | Type | Control |
|-----------|------|---------|
| Tower Cooler | Copper heat pipes + aluminum fins | Passive (attached to CPU) |
| CPU Fan | 4-pin PWM fan | Pi 5 firmware — automatic curve based on CPU temp |
| GPIO Fans | 2× 40×40×10mm 5V fans (2-pin) | `pironman5` service, shared GPIO6 control pin |

- Default CPU fan curve: < 50 °C off → 50 °C 30% → 60 °C 50% → 67.5 °C 70% → ≥ 75 °C 100%.
- Customizable via `dtparam=fan_temp0=...` in `/boot/firmware/config.txt`.
- GPIO fan modes: Always On, Performance (50 °C), Cool (60 °C), Balanced (67.5 °C), Quiet (70 °C).
- Under 100% load, Pi 5 stays at ~39 °C in a 25 °C room.

## Display
- **0.96" OLED**, 128×64 resolution, I2C (address `0x3C`).
- Pages: `mix` (CPU/RAM/IP/temp), `performance`, `ips` (IP info), `disk`.
- Sleep timeout configurable (default 10 s); wake via power button (v1.3.6+) or vibration switch (older).
- Rotation: 0° or 180°.

## Lighting
- **4× WS2812-5050 addressable RGB LEDs** (driven by SPI via GPIO10).
- RGB OUT pins for chaining external WS2812 strips — update `rgb_led_count` accordingly.
- 2× GPIO fan LED control (GPIO5, can be set `on`/`off`/`follow`).
- Effects: solid, breathing, flow, flow_reverse, rainbow, rainbow_reverse, hue_cycle.

## Storage & Expansion — Dual NVMe PIP
- **ASM1182e PCIe Gen2 switch** — splits Pi 5's single Gen2 x1 lane into two independent lanes.
- **Two M.2 M-key slots**: supports 2230 / 2242 / 2260 / 2280 sizes.
- Use cases:
  - Dual NVMe SSDs (RAID 0/1 for NAS)
  - SSD + Hailo-8/8L AI accelerator
  - Dual AI accelerators
- **Bandwidth**: ~500 MB/s per slot (shared from Pi 5's PCIe Gen2).
- **PCIe Gen3 not supported**.
- FFC/FPC cable connects Dual NVMe PIP to Pi 5.
- Onboard 3.3 V/3 A regulator; auxiliary 5 V via J3 connector for high-power loads.
- J4 "FORCE ENABLE" solder pads for systems without PCIe switch signal.

## Connectivity
- 2× USB 2.0, 2× USB 3.0
- Gigabit Ethernet (RJ45)
- 2× 4Kp60 full-size HDMI ports (rear-aligned)
- USB-C power input
- Raspberry Pi standard 40-pin GPIO (extended via right-angle headers with labels)
- Spring-loaded microSD slot

## I/O Board Features
| Component | GPIO | Notes |
|-----------|------|-------|
| IR Receiver (IRM-56384, 38 kHz) | GPIO13 | Jumper J8 to enable/disable |
| RGB LEDs (WS2812-5050) | GPIO10 (SPI MOSI) | Jumper J9 area |
| OLED Display | I2C (SDA/SCL) | Address 0x3C |
| GPIO Fans (2× 2-pin) | GPIO6 | Jumper-controlled |
| Fan LEDs | GPIO5 | Jumper-controlled |
| Vibration Switch | Shared | Wake OLED; remove jumper post-v1.3.6 |
| External GPIO | 40-pin header | Extended via right-angle breakouts |

- Removing jumpers frees the corresponding GPIO for other uses.
- Solder bridge option available for always-on fan/LED (bypasses GPIO control).

## Multimedia
- IR receiver (38 kHz) for media-center remote control (Kodi, Volumio, etc.)

## Optional Configurations
- **RTC**: 1220 battery socket for real-time clock.
- **Boot from NVMe**: Supported — configure boot order in Pi 5 EEPROM.
- **Home server roles**: NextCloudPi, OpenMediaVault, Plex, OpenClaw.
- **Dashboard**: Web UI at `http://<ip>:34001`; installable with or without (`--disable-dashboard`).

## Compatible Systems (tested)
Raspberry Pi OS (Desktop & Lite), Ubuntu, Kali Linux, Homebridge, Home Assistant, Umbrel OS.

## Incompatible
- **Raspberry Pi AI HAT+** — does not fit the case. Use the Hailo module directly in the M.2 slot instead.
- **NVMe SSDs with Phison E27T/E21 controllers** — instability reported.
- **Gen3 PCIe devices** — Pi 5 implements Gen2 only.

## Quick Specs Summary
| Parameter | Value |
|-----------|-------|
| Dimensions | 111.9×78.5×117 mm |
| Material | Aluminum alloy + acrylic panels |
| Platform | Raspberry Pi 5 |
| Power | USB-C 5V/5A (27W PD recommended) |
| OLED | 0.96" 128×64 I2C |
| RGB LEDs | 4× WS2812-5050 + expansion via RGB OUT |
| NVMe Slots | 2× M.2 M-key (2230-2280), PCIe Gen2 |
| CPU Fan | 4-pin PWM, firmware-controlled |
| GPIO Fans | 2× 40mm, GPIO6-controlled |
| IR Receiver | 38 kHz, GPIO13 |
| RTC Battery | 1220 |
