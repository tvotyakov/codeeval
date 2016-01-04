#!python3
import struct
print('LittleEndian' if struct.pack('=I', 2**31 - 1) == b'\xFF\xFF\xFF\x7F' else 'BigEndian')
