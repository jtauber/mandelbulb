H = 600
W = 600

# just do as a dictionary as it starts off sparse
heights = {}

for height in range(54, -1, -1):
    print "height %d" % height
    filename = "mandel8_%02d.values" % height
    
    f = open(filename)
    
    header = f.readline()
    assert header == "H %s W %s\n" % (H, W), header
    
    for xx in range(W):
        for yy in range(H):
            value = int(f.readline().strip())
            
            if value == 0 and (xx, yy) not in heights:
                heights[xx, yy] = height


import zlib
import struct
import array
from math import sqrt, atan2, cos, sin

def output_chunk(out, chunk_type, data):
    out.write(struct.pack("!I", len(data)))
    out.write(chunk_type)
    out.write(data)
    checksum = zlib.crc32(data, zlib.crc32(chunk_type))
    out.write(struct.pack("!I", checksum))

def get_data(width, height, rgb_func):
    compressor = zlib.compressobj()
    data = array.array("B")
    for y in range(height):
        data.append(0)
        for x in range(width):
            data.extend([min(255, max(0, v)) for v in rgb_func(x, y)])
    compressed = compressor.compress(data.tostring())
    flushed = compressor.flush()
    return compressed + flushed

def write_png(filename, width, height, rgb_func):
    out = open(filename, "w")
    out.write(struct.pack("8B", 137, 80, 78, 71, 13, 10, 26, 10))
    output_chunk(out, "IHDR", struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0))
    output_chunk(out, "IDAT", get_data(width, height, rgb_func))
    output_chunk(out, "IEND", "")
    out.close()


def func(x, y):
    c = 4 * heights.get((x, y), 63)
    return c, c, c


write_png("heightfield.png", W, H, func)