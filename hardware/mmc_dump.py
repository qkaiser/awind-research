#!/usr/bin/env python
"""
Dump MMC memory from Airmedia AM-100 or similar devices.

# Dumping process steps

    * drop to u-boot shell
    * sanity check with printenv
    * load 512 bytes memory chunk from MMC to RAM at known safe address with "mmcread"
    * display 512 bytes of memory from RAM at known safe address with "md.b"
    * convert dumped hex to binary and write to output file

# Limitations

    In experimental settings, the fastest I got was something around 2kB/sec.
    It takes approximately 20 days to do a full dump (I"m not joking).

# Requirements

    You need picocom to connect to the serial device. pexpect does not play
    well with 'screen'.

Author: Quentin Kaiser <kaiserquentin@gmail.com>
"""
import pexpect
import sys
import re
import binascii
import time

BLOCKS=7733248
BLOCK_SIZE=512
RAM_ADDRESS=20971520 #0x1400000
PROMPT="WMT"

def dump(serial_device, dump_file):
    """
    Connects to <serial_device> and dumps MMC to <dump_file>.

    Args:
        serial_device(str): serial device (e.g. /dev/ttyUSB0)
        dump_file(str): file path where memory will be dumped

    Returns:
        None
    """
    try:
        output_file = open(dump_file, "wb")
        print("[+] Setting up serial line.")
        child = pexpect.spawn("picocom --nolock -b 115200 %s" % serial_device)
        child.sendline('')
        child.expect(PROMPT)
        print("[+] Initializing MMC ...")
        child.sendline('mmcinit 1')
        child.expect(PROMPT)
        print("[+] Starting dumping process ...")
        for i in range(0, BLOCKS):
            # read memory to RAM
            child.sendline("mmcread 1 0x%07x 0x%08x 0x%03x" % (RAM_ADDRESS, i, BLOCK_SIZE))
            child.expect(PROMPT)
            # display memory in hex dumps
            child.sendline("md.b 0x%07x 0x%03x" % (RAM_ADDRESS, BLOCK_SIZE))
            child.expect(PROMPT)
            # get output and dump it to file after proper conversion
            output = child.before.strip()
            for m in re.findall(r"[0-9a-z]+:( [0-9a-z ]{47})", output):
                l = [binascii.unhexlify(x) for x in m.split()]
                output_file.write("".join(l))
            sys.stdout.write("\r[o] %d/%d blocks read" % (i, BLOCKS))
            sys.stdout.flush()
        print("[+] Dumping done (finally !)")
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        output_file.close()
        child.close()
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s serial_device dump_file" % (sys.argv[0]))
        sys.exit(1)
    dump(sys.argv[1], sys.argv[2])
