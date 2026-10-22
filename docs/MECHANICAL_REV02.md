# Rev0.2: Mechanical extension and validation requirements

> **Updated interpretation (2026-10-23 audit):** the 6.20 +/- 0.20mm cited below is the USB Type-C **receptacle effective shell length**, NOT a specified exposed PCB tongue protrusion. The 6.200mm geometry is retained as a **provisional experimental dimension**, pending cable insertion and pad-contact tests. Nominal 0.8mm FR-4 also differs from the USB-IF nominal 0.70 +/- 0.05mm tongue thickness and should not be called USB mechanically compliant. See [PRIOR_ART_AUDIT_2026-10-23.md](PRIOR_ART_AUDIT_2026-10-23.md).

## Geometry (millimeters)

| Dimension | Rev0.1 | Rev0.2 |
| --- | ---: | ---: |
| Board tip X | -4.950 | -6.835 |
| Root shoulder X | -0.635 | -0.635 |
| Tip to shoulder | 4.315 | **6.200** |
| Added length | 0 | **+1.885** |
| Nominal tongue width | 6.690 | 6.690 |
| Narrow tip width | 6.095 | 6.095 |

The pads, nose chamfer and original lateral latch notches move forward 1.885mm. Pad dimensions and each pad's position *relative to the tip* are unchanged. The straight neck leading to the PCB shoulder is extended. Edge.Cuts integration points remain (-0.635,-4.450) and (-0.635,+4.445). No rear attachment pads, holes, silkscreen frame or paste openings are created.

**Reason for 6.20mm**: the USB Type-C connector specification mentions 6.20 +/- 0.20mm *effective receptacle shell length*, not an explicitly specified exposed PCB tongue length. Using 6.20mm for a no-shell PCB edge receptacle is an engineering **hypothesis** to reduce premature stoppage and insufficient mating. It does not establish USB-IF mechanical compliance or prove the plug will seat fully.

## Board thickness and manufacturing

The **nominal PCB thickness baseline is 0.8mm, with two FR-4 copper layers and ENIG contact finish**, for both 14P USB 2.0 and 10P power-only variants. This is the selected design requirement; it is not proof of actual mating. The USB Type-C receptacle tongue nominal thickness is about 0.70 +/- 0.05mm. Before ordering, check fabrication thickness tolerances (e.g. +/-0.1mm where offered), since thicker boards can bind and thinner ones may give poor contact force. External prototype material includes a 0.6mm build and an 0.8mm design reference; here 0.6mm is kept only as a fallback for separate comparative tests, **not as a co-equal baseline**. Manufacturing feasibility and 0.8mm mating/firmware uploading have **not been verified**. Do not add soldermask, silkscreen or extra layers in the contact zone.

## Electrical pin types (symbol ERC)

- `VBUS` and `GND`: `power_in` (USB connector is not assumed to be a permanently active source; use PWR_FLAG only at verified power-source nets, as needed).
- `CC1`, `CC2`, `D+`, `D-`: `bidirectional`. For a 5V USB-C sink CC1 and CC2 each require independent 5.1kΩ Rd to ground.
- Data pins are absent from the power-only 10-pin model. Check the actual ESP32 USB peripheral and any power-path protection for the connected board.

## Pending physical verification

1. Check at least two different USB-C cables in both orientations; visually confirm no shoulder or enclosure interference before full mating.
2. Verify contact continuity at VBUS, GND, CC1/CC2 and D+/D- while held stationary.
3. Verify USB2 enumeration and ESP32 firmware upload on the 14-pin design.
4. Check interruption susceptibility, PCB flex, USB-plug spring latch engagement and tolerance variation.
5. Open in KiCad 10.x; ensure Edge.Cuts closes only after connection to the main-board outline; perform ERC/DRC and Gerber review.

**These checks are not performed by this change.** The 0.8mm baseline is a design choice, not proof of mating/contact quality or successful firmware upload. Keep 0.6mm as a nonstandard alternative if testing requires it.

## Sources

- USB Type-C Cable and Connector Specification, Release 2.4 (October 2024).
- https://github.com/AnasMalas/pcb-edge-usb-c (prototype and thickness cautions).
- https://jlcpcb.com/capabilities/pcb-capabilities/ (manufacturing tolerance).
- Original footprint geometry: https://github.com/vasya-zh/PCB-Edge-USB-connector-KiCad-library (GPL-3.0; attribution retained).
