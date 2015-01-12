class Karatsuba:
    def multiply(self, ix, iy):
        # If integers are two digits or less
        if len(ix) <= 2 or len(iy) <= 2:
            return int(ix) * int(iy)
        else:
            # Turn integers to lists
            x = list(ix)
            y = list(iy)
            
            # Pad lists until they are even length
            if len(x) % 2:
                x.insert(0, '0')
            if len(y) % 2:
                y.insert(0, '0')
                
            nx = len(x)
            ny = len(y)
            print "Integer X: " + str(x)
            print "Integer Y: " + str(y)

            # Split into parts
            a = x[0:nx/2]
            b = x[nx/2:]
            c = y[0:ny/2]
            d = y[ny/2:]
            
             # Pad parts until they are even length
            if len(a) % 2:
                a.insert(0, '0')
            if len(b) % 2:
                b.insert(0, '0')
            if len(c) % 2:
                c.insert(0, '0')
            if len(d) % 2:
                d.insert(0, '0')
                
            print "Part A: " + str(a)
            print "Part B: " + str(b)
            print "Part C: " + str(c)
            print "Part D: " + str(d)
 
            # Recursively get product
            return 10 ** ((nx + ny)/2) * self.multiply(''.join(a),''.join(c)) + 10 ** (nx/2) * self.multiply(''.join(a),''.join(d)) + 10 ** (ny/2) * self.multiply(''.join(b),''.join(c)) + self.multiply(''.join(b),''.join(d))
    

# usage
multiplier = Karatsuba()
print multiplier.multiply("12345","1234567")
