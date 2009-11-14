/*
from math import sqrt, atan2, cos, sin
*/

package main

import "math"
import "fmt"
import "os"

const (
    n = 8;
    h = 100;
    w = 100;
)

func mandel(x0 float64, y0 float64, z0 float64) int {
    
    x := float64(0.0);
    y := float64(0.0);
    z := float64(0.0);
    
    for i := 0; i < 32; i++ {
        
        r := math.Sqrt(x*x + y*y + z*z);
        theta := math.Atan2(math.Sqrt(x*x + y*y), z);
        phi := math.Atan2(y, x);
        
        x = math.Pow(r, n) * math.Sin(theta * n) * math.Cos(phi * n) + x0;
        y = math.Pow(r, n) * math.Sin(theta * n) * math.Sin(phi * n) + y0;
        z = math.Pow(r, n) * math.Cos(theta * n)                     + z0;
        
        if x*x + y*y + z*z > 2 {
            return 256 - (i * 4);
        }
    }
    
    return 0;
}

func main() {
    
    for layer := 0; layer < 100; layer++ {
        
        fmt.Printf("layer %d\n", layer);
        
        filename := fmt.Sprintf("mandel8_%02d.values", layer);
        
        f, err := os.Open(filename, os.O_WRONLY | os.O_CREATE, 0666);
        
        if err != nil {
            fmt.Printf("got error\n");
            return;
        }
        
        fmt.Fprintf(f, "H %d W %d\n", h, w);
        
        for xx := 0; xx < w; xx++ {
            for yy := 0; yy < h; yy++ {
                x := float64(4 * (xx - (w / 2))) / float64(w);
                y := float64(4 * (yy - (h / 2))) / float64(h);
                z := float64(layer) / 50.0;
                var m int = mandel(x, y, z);
                fmt.Fprintf(f, "%d\n", m);
            }
        }
        
        f.Close();
    }
}