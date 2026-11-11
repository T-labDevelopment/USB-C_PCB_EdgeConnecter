# USB-C PCB Edge CR2032 Cable-Insert LED Tester

**Cable connection itself is the ON switch.** No pushbuttons or other operating switches.

- **One board**: USB-C PCB-edge 14P ×2 (J1/J2), 10P ×2 (J3/J4); two independent USB-C to USB-C **passive, unpowered** cable loops
- **Power**: CR2032 ×1 (BT1), shared by both loops
- **Indicators**: two low-current red LEDs (D1/D2), one for each connector pair
- **Current limit**: 2.2kΩ (R1/R2), one per LED loop
- **Board**: nominal FR-4 0.8mm, two layers, ENIG, 6.2mm protrusion, no silk around contact tongues

## What happens

| 14P cable (J1→J2) | 10P cable (J3→J4) | LEDs |
|---|---|---|
| Absent | Absent | Both off |
| Connected | Absent | D1 on, D2 off |
| Absent | Connected | D1 off, D2 on |
| Connected | Connected | Both on |

### Serial test paths

14P: CR2032+ → R1 → J1 VBUS → cable → J2 VBUS → CC → cable → J1 CC → D+ → cable → J2 D+ → D− → cable → J1 D− → GND → cable → J2 GND → D1 anode → cathode → CR2032−.

10P: CR2032+ → R2 → J3 VBUS → cable → J4 VBUS → CC → cable → J3 CC → GND → cable → J4 GND → D2 anode → cathode → CR2032−.

**LEDs light whenever the corresponding cable completes the loop and there is no open connection.** Disconnect the cable to switch off and save battery; leaving both connected causes continuous battery drain.

### Safety / limits

This board is a battery-powered electrical **test fixture**, NOT a USB host, device or USB-PD circuit. The connector CC1/CC2 pads are intentionally bridged. **Never connect to a computer, charger, power bank, USB-enabled board, or external power source, especially with CR2032 installed. Use passive C-to-C cables only.**

The LED tests only **grouped serial continuity**, not every redundant contact, actual USB2 enumeration, signal integrity, PD negotiation, shorts between unselected nets, or reliable firmware flashing. Flip each cable end separately and test both orientations; some active/e-marked cables may not support the fixture's CC test. Select low-current high-brightness red LEDs.

CR2032 standard continuous current is typically about 0.2mA (Panasonic); a 2.2kΩ series resistor and red LED can demand several tenths of a milliampere. Intermittent testing is recommended. No extra switch is installed by design.

### Build status

The KiCad schematic, BOM and **footprint placement** are updated. **The PCB traces remain unrouted (0 copper segments).** The CAD files have not passed native KiCad 10 ERC/DRC or physical validation, and the 0.17mm GND contact to Edge.Cuts issue remains. **Do not order as a functional PCB yet.**

The older 6-LED/6-button study remains under `../USB_C_Loop_Tester`; it is not the preferred prototype.

### References
- https://developerhelp.microchip.com/xwiki/bin/view/applications/usb/typec-features/cc-vconn-signals/
- https://energy.panasonic.com/jp/business/products/lithium/coin-cr-standard/models/CR2032
- https://github.com/AnasMalas/pcb-edge-usb-c
