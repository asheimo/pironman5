# Pironman 5 Mini Hardware Snapshot

## Quick facts
- **Form factor:** 67.8 × 98.6 × 101.5 mm (notably shorter and narrower than the standard/Max cases).
- **Materials:** Silver aluminum chassis with smoked acrylic side panels.
- **Display:** *No built-in OLED.* All telemetry lives in the dashboard or via connected displays.
- **Cooling:** Active top-down cooler similar to the official Raspberry Pi unit plus a single RGB 40×40×10 mm side fan tied to the WS2812 bus.
- **Lighting:** 4 × WS2812-5050 LEDs + RGB side fan (total 5 controllable endpoints by default).
- **Controls:** One metal power button, RTC (CR1220), and exposed GPIO extender.
- **IO layout:**
  - 2 × USB 2.0, 2 × USB 3.0, Gigabit Ethernet, USB-C power.
  - 2 × 4Kp60 *micro* HDMI ports (carry a spare adapter!)
  - Spring-loaded MicroSD slot.
- **Storage:** Single PCIe 2.0 M.2 M‑key slot (2230/2242/2260/2280) for NVMe SSDs; supports PCIe AI accelerators with adapters.
- **Power:** USB-C 5 V/5 A (27 W PSU recommended, even though the case is smaller).

## Thermal + airflow notes
- The compact shell leaves less headroom above the cooler; avoid stacking objects directly on top.
- The RGB side fan pulls air across the NVMe slot—keep cables clear to maintain flow.
- Because there is no tower cooler, SOC temps respond faster to load swings; tune fan curves accordingly in the dashboard.

## When to choose the Mini
- You need a space-saving chassis but still want NVMe + RGB effects.
- OLED readouts are optional (you rely on dashboard monitoring or external displays).
- Travel / demo rigs where the full-height tower cooler is impractical.
