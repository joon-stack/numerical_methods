import math

def composite_trapezoidal(lb, rb, seg):
    sum = 0.0
    length = rb - lb
    size = length / seg

    def v(t):
        g = 9.8
        m = 68.1
        c = 12.5
        return g * m / c * (1 - math.exp(-c / m * t))

    sum = v(lb)

    for i in range(1, seg):
        t = lb + i * size
        sum += 2 * v(t)
        
    
    sum += v(rb)
    res = size * sum / 2
    
    return res, size

def main():
    exact = 289.43515
    segments = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    for seg in segments:
        res, size = composite_trapezoidal(0, 10, seg)
        error = abs((exact - res) / exact)
        print("Segments: {0} | Segment size: {1} | Estimated d (m): {2:.4f} | Relative Error (%): {3:}".format(seg, size, res, error * 100))


if __name__ == "__main__":
    main()


