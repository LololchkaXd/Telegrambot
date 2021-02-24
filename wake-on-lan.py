#!/usr/bin/env python3
import wakeonlan

from wakeonlan import send_magic_packet
send_magic_packet('00:1c:c0:7b:ec:66', ip_address='176.108.102.212', port=9)

print('All done')            



