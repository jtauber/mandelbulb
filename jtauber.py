from math import sqrt, atan2, cos, sin
import sys


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

def main(h, w):
    for layer in range(100):
        
        print "layer %d" % layer
        
        f = open("mandel8_%02d.values" % layer, "w")
        
        f.write("H %d W %d\n" % (h, w))
        for xx in range(w):
            for yy in range(h):
                x = 4.0 * (xx - (w / 2.0)) / w
                y = 4.0 * (yy - (h / 2.0)) / h
                z = layer / 50.0
                m = mandel(x, y, z)
                f.write("%d\n" % m)
        
        f.close()

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[1]))
