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


n = 8

def mandel(x0, y0, z0):
    
    x, y, z = 0.0, 0.0, 0.0
    
    for i in range(32):
        
        r = sqrt(x*x + y*y + z*z)
        theta = atan2(sqrt(x*x + y*y), z)
        phi = atan2(y, x)
        
        x = r**n * sin(theta*n) * cos(phi*n) + x0
        y = r**n * sin(theta*n) * sin(phi*n) + y0
        z = r**n * cos(theta*n)              + z0
        
        if x**2 + y**2 + z**2 > 2:
            return 256 - (i * 4)
    else:
        return 0

h = 600
w = 600

for layer in [21]:
    print "layer %02d" % layer
    
    def mandelbrot_function(xx, yy):
        x = 4.0 * (xx - (w / 2.0)) / w
        y = 4.0 * (yy - (h / 2.0)) / h
        z = layer / 50.0
        m = mandel(x, y, z)
        return (m,m,m)
    
    write_png("mandel8_%02d.png" % layer, w, h, mandelbrot_function)
