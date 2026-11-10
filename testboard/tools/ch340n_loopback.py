#!/usr/bin/env python3
# Rev.T1 14P USB-C edge test board: CH340N RTS LED + UART loopback.
# Requires pyserial==3.5; no network/other hardware.
# Test with only J1 connected; close SJ1 before loopback.
import argparse
import sys
import time

import serial


def run(port: str, baud: int, blink_count: int, skip_loopback: bool) -> int:
    try:
        with serial.Serial(
            port=port, baudrate=baud, timeout=1.5, write_timeout=1.5,
            rtscts=False, dsrdtr=False
        ) as ser:
            print(f"OPEN {ser.port} at {baud} baud (CH340N identification must be checked separately)")
            # CH340N RTS# is active LOW: pyserial RTS=True asserts RTS.
            ser.rts = False
            time.sleep(0.25)
            for index in range(blink_count):
                ser.rts = True
                time.sleep(0.35)
                ser.rts = False
                time.sleep(0.35)
                print(f"RTS LED toggle {index+1}/{blink_count} (verify LED3 visually)")

            if skip_loopback:
                print("Loopback skipped; USB data communication unverified")
                return 0

            # SJ1 is a solder bridge between TXD and RXD: close for this test.
            payload = b"USB_EDGE_REV_T1_LOOPBACK_12345\r\n"
            ser.reset_input_buffer()
            count = ser.write(payload)
            ser.flush()
            received = ser.read(len(payload))
            ok = (count == len(payload) and received == payload)
            print(f"Sent {count} bytes, read {len(received)} bytes")
            print(f"UART LOOPBACK: {'PASS' if ok else 'FAIL'}")
            if not ok:
                print(f"Expected: {payload!r}\nReceived: {received!r}", file=sys.stderr)
            return 0 if ok else 1
    except (serial.SerialException, OSError) as exc:
        print(f"PORT ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CH340N USB-C PCB edge 14P RTS LED and UART loopback test"
    )
    parser.add_argument("--port", required=True, help="e.g. COM5 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--blinks", type=int, default=3)
    parser.add_argument("--skip-loopback", action="store_true")
    args = parser.parse_args()
    if args.baud <= 0 or args.blinks < 0:
        parser.error("baud must be positive and blinks nonnegative")
    return run(args.port, args.baud, args.blinks, args.skip_loopback)


if __name__ == "__main__":
    raise SystemExit(main())
