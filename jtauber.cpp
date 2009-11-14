#include <fstream>
#include <iostream>
#include <cmath>
#include <sstream>

#define n 8


std::string int_to_string(int i) {
    std::stringstream s;
    s << i;
    return s.str();
}

int string_to_int(std::string s) {
    std::istringstream ss(s);
    int i;
    ss >> i;
    return i;
}

int mandel(float x0, float y0, float z0) {
    float x = 0.0;
    float y = 0.0;
    float z = 0.0;
    
    for (int i = 0; i < 32; i++) {
        float r = sqrt(x*x + y*y + z*z);
        float theta = atan2(sqrt(x*x + y*y), z);
        float phi = atan2(y, x);
        
        x = pow(r, n) * sin(theta * n) * cos(phi * n) + x0;
        y = pow(r, n) * sin(theta * n) * sin(phi * n) + y0;
        z = pow(r, n) * cos(theta*n);
        
        if (x*x + y*y + z*z > 2) {
            return 256 - (i * 4);
        }
    }
    return 0;
}

int main(int argc, char* argv[]) {
    int h, w;
    h = w = string_to_int(argv[1]);
    for (int i = 0; i < 100; i++) {
        std::cout << "layer " << i << std::endl;
        std::ofstream f;
        f.open(("madel8_" + int_to_string(i) + ".values").c_str());
        for (int xx = 0; xx < w; xx++) {
            for (int yy = 0; yy < h; yy++) {
                float x = 4.0 * (xx - (w / 2.0)) / w;
                float y = 4.0 * (yy - (h / 2.0)) / h;
                float z = i / 50.0;
                f << mandel(x, y, z);
            }
        }
        f.close();
    }
}
