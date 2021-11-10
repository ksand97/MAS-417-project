from stl_generation import stl_generator_12p
import api_info


y=api_info.Y

y1=10e-3*y[0]
y2=10e-3*y[1]
y3=10e-3*y[2]
y4=10e-3*y[3]
y5=10e-3*y[4]
y6=10e-3*y[5]
y7=10e-3*y[6]
y8=10e-3*y[7]
y9=10e-3*y[8]
y10=10e-3*y[9]
y11=10e-3*y[10]
y12=10e-3*y[11]


if __name__ == "__main__":
    stl_generator_12p.stl_generator(y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12)



