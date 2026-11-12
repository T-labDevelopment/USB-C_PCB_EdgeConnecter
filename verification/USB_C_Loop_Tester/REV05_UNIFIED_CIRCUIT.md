# Rev.0.5 — USB-C 14P/10P six-indicator unified loop tester

Date: 2026-11-12. Base: user-provided rough circuit image and the Rev.0.4 KiCad test fixture. This document defines the *logical cable-test circuit*; it is not a fabricated-board acceptance report.

## Design rules
1. A battery CR2032 drives independent branches through `R1–R6 = 22kΩ`.
2. Each branch leaves its **source connector**, crosses the matching wire in an **unpowered passive C-C cable**, enters the corresponding **receiver connector** and its own LED anode, then returns to the battery via the cable's GND conductor.
3. Connector pairs are J1/J2 (14P) and J3/J4 (10P). Their source-side GND nets share BAT_NEG because one battery is used, but their receiver GND nets remain independent (`RET_T14`, `RET_T10`).
4. Never directly short the source-to-receiver signal or GND nets on the PCB, as doing so would make an LED light without a cable.
5. Same-function A/B pins are grouped on each connector: VBUS A4/A9/B4/B9; CC1/CC2 A5/B5; D+ A6/B6 and D− A7/B7 for 14P; GND A1/A12/B1/B12. These groups have only one LED each.
6. This **test fixture only** intentionally connects CC1/CC2; it is not a USB-C compliant host/device implementation. The product-use USB symbols have not been altered.

## Explicit net-level paths

| LED | Source resistor | Source | Cable path | Receiver | LED K / return |
|---|---|---|---|---|---|
| D1 VBUS | R1 | J1 VBUS | 14P VBUS | J2 VBUS | RET_T14 via J2 GND |
| D2 CC | R2 | J1 CC1/CC2 | 14P active CC | J2 CC1/CC2 | RET_T14 |
| D3 D+ | R3 | J1 D+ A/B | 14P USB D+ | J2 D+ A/B | RET_T14 |
| D4 D− | R4 | J1 D− A/B | 14P USB D− | J2 D− A/B | RET_T14 |
| D5 VBUS | R5 | J3 VBUS | 10P VBUS | J4 VBUS | RET_T10 via J4 GND |
| D6 CC | R6 | J3 CC1/CC2 | 10P active CC | J4 CC1/CC2 | RET_T10 |

In each row `CR2032+ → resistor → source connector → cable → receiver connector → LED(A→K) → receiver GND → cable GND → source GND → CR2032−`.

The schematic has no internal J1-J2 / J3-J4 bridge. Insertion of a real passive cable supplies the only possible electrical bridges.

## Ideal cable continuity truth table

| Connected cable(s) / simulated fault | D1 | D2 | D3 | D4 | D5 | D6 |
|---|---|---|---|---|---|---|
| None | OFF | OFF | OFF | OFF | OFF | OFF |
| 14P only | ON | ON | ON | ON | OFF | OFF |
| 10P only | OFF | OFF | OFF | OFF | ON | ON |
| Both | ON | ON | ON | ON | ON | ON |
| Both, 14P D+ open | ON | ON | OFF | ON | ON | ON |
| Both, 14P GND open | OFF | OFF | OFF | OFF | ON | ON |
| Both, 10P CC open | ON | ON | ON | ON | ON | OFF |
| Both, 10P GND open | ON | ON | ON | ON | OFF | OFF |

**Result:** all eight modeled cases matched the expected LEDs using resistor interconnects, forward LED orientation and cable/GND presence. Model assumes ideal passive conductors; it does not prove USB enumeration, USB signal integrity, or individual redundant-contact quality.

## Basic electrical calculation and constraints

For a nominal 3.0V CR2032, 22kΩ resistor and assumed red LED Vf≈1.8V: `I≈(3.0−1.8)/22000≈0.055mA` per channel; all six simultaneously ≈0.33mA, ignoring battery internal resistance. **This is an estimate, not a measurement or LED photometric guarantee.** A battery's standard continuous drain rating of 0.2mA is not an absolute maximum. Use short-duration tests; unplug both cables after testing. Inspect LED optical brightness in the real prototype before reducing current-limit resistance.

Sources:
- Panasonic CR2032 3V / 0.2mA continuous standard drain: https://energy.panasonic.com/jp/business/products/lithium/coin-cr-standard/models/CR2032
- CC1/CC2 orientation and one active CC wire: https://developerhelp.microchip.com/xwiki/bin/view/applications/usb/typec-features/cc-vconn-signals/

## File checks / validation truth

- Existing **KiCad 10** .kicad_sch and .kicad_pcb; full local `USB_C_PCB_Edge` symbols/footprints are retained.
- Schematic: **17 instances, 74 pin positions, 85 wire segments, 18 junctions, 16 connected net groups, zero labels**. All wires and pins on a 50mil grid. Zero missing pin endpoints; zero mixed-net graph nodes; zero disconnected groups; zero geometric wire crossings.
- PCB: **17 footprints, 74 pads, 0 copper trace segments**. The PCB has not been routed; **it will not operate if fabricated as-is.**
- Static cable/polarity model: PASS for 8 scenarios shown above.
- **KiCad-native ERC/DRC: NOT RUN** (no KiCad executable in this runtime). Do not claim ERC0 / DRC0, verified optical brightness or completed Gerbers.
- Rev.0.5 is saved to its own Git working branch. Main untouched until explicitly integrated.
