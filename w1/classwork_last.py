def compute_distance(p1, p2):
    sqrd_sum = 0
    if len(p1)==len(p2):
        for dimnsn in range(len(p1)):
            sqrd_sum += (p1[dimnsn] - p2[dimnsn])**2
    else:
        print("not equal dimensions")

    return sqrd_sum**0.5    


def compute_for_circle(x0=9,y0=3,x1=6,y1=8,x2=3,y2=6):
    point_dict = {'a':((x0,y0),(x1,y1)),
                  'b':((x1,y1),(x2,y2)),
                  'c':((x0,y0),(x2,y2))
        }
    a=compute_distance((x0,y0),(x1,y1))
    b=compute_distance((x1,y1),(x2,y2)) 
    c=compute_distance((x0,y0),(x2,y2))

    half_per = (a+b+c)/2
    triangle_area = (half_per*(half_per-a)*(half_per-b)*(half_per-c))**0.5
    radius = (a*b*c)/(4*triangle_area)

    print(a,b,c)
    print(radius)

    numerator = x2**2 + y2**2 - x1**2 - y1**2 - ((x1**2 + y1**2 - x0**2- y0**2)*(x2 - x1)/(x1-x0))
    denominator = 2*y2 - 2*y1 + ((y0 - y1)*(2*x2 - 2*x1)/(x1 - x0))
    y_center = numerator/denominator

    x_center = ((y0-y1)/(x1-x0))*y_center + ((x1**2 + y1**2 - x0**2 - y0**2)/(2*x1-2*x0))

    print(x_center, y_center)

    return x_center, y_center, radius

compute_for_circle()