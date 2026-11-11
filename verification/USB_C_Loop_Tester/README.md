# CR2032 USB-C cable loop tester (draft)

**Design**: 1 PCB, four integrated PCB-edge USB-C contacts (14P x2, 10P x2), two separately connected passive C-to-C USB cables. One CR2032, six pushbuttons, six 2.2k resistors, six low-current red LEDs.

Press **only one button at a time**. Current flows:
`CR2032 + → PUSH → 2.2k → source USB signal → C-to-C cable → return USB signal → LED anode → LED cathode → isolated return USB GND → C-to-C cable → source USB GND → CR2032 –`.

The receiving connector's GND network is **not connected to BAT_NEG on the PCB**. This is deliberate; it forces cable-ground continuity.

| Button | LED | 2-pin port pair | Tests |
| --- | --- | --- | --- |
| SW1 | D1 | J1 ⇄ J2 (14P) | VBUS with GND return |
| SW2 | D2 | J1 ⇄ J2 (14P) | CC1/CC2 using the active CC cable conductor, with GND return |
| SW3 | D3 | J1 ⇄ J2 (14P) | USB D+, with GND return |
| SW4 | D4 | J1 ⇄ J2 (14P) | USB D−, with GND return |
| SW5 | D5 | J3 ⇄ J4 (10P) | VBUS with GND return |
| SW6 | D6 | J3 ⇄ J4 (10P) | CC1/CC2 with GND return |

- Source-side CC1 and CC2 are shorted to one test signal **only on this powerless cable tester**; receiver-side CC1/CC2 are similarly shorted to one LED. This fixture is **not** a normal compliant USB device or PD implementation.
- 14P A6/B6 share one D+ net; A7/B7 share one D− net, by design for reverse-plug coverage.
- All four connector GND pads at the source are tied to battery negative; receiver GND is isolated so a damaged cable ground interrupts the indicator.
- If multiple LEDs illuminate for a single button, suspect an unintended short between conductors; if none illuminate, check battery/LED/polarity and cable position.
- **The lights do not prove all individual redundant VBUS/GND pads work** or show low-resistance contact quality. Cable plug reversal on **each end individually** is mandatory to exercise CC orientation.
- **NEVER attach a PC, USB charger, PD source, powered USB device, or external power** while CR2032 is fitted. Test **unpowered C-to-C cables only**. A cable carrying active electronics may not behave as an ordinary passive cable.
- 2.2k current limiting resistor constrains short current to at most ~1.4mA with a fresh 3.0V cell. Red LED current roughly 0.2-0.6mA, dependent on LED and cell; low-current LED required. FDK CR2032 standard discharge current is 0.2mA; buttons are intended for momentary tests.
- Intended PCB: FR-4 2 layers, nominal 0.8mm, ENIG, with 6.2mm edge tabs and no contact-zone silkscreen. Inner board can have normal component labels.
- Footprint reference geometry and pin names are reused from the project's current USB_C_PCB_Edge library; standard device symbols are the canonical embedded Device/Switch definitions used by KiCad.
- **Validation status**: native schematic generated, but KiCad 10 CLI/GUI and ERC/DRC have not been run. Do not order without PCB routing, mechanical fit and DRC.
- Tests: press all 6 buttons with each cable orientation; for CC, flip **both ends**, one at a time. Record LED result and insertion depth.

References:
- Microchip USB Type-C pin signals: https://developerhelp.microchip.com/xwiki/bin/view/applications/usb/typec-features/cable-connector/
- Richtek cable CC/VCONN wiring: https://www.richtek.com/Home/Design%20Support/Technical%20Document/AN056
- FDK CR2032 datasheet: https://www.fdk.co.jp/battery/lithium/data_sheet/CR2032_Data-sheet.pdf
- KiCad 10: https://www.kicad.org/blog/2026/10/KiCad-10.0.7-Release/
