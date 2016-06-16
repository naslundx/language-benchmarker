use math

A := FloatMatrix new(8, 8) take()
B := FloatMatrix new(8, 8) take()
C := FloatMatrix new(8, 8) take()
D := FloatMatrix new(8, 8) take()
E := FloatMatrix new(8, 8) take()

generator := FloatUniformRandomGenerator new()

for (i in 0 .. A width)
    for (j in 0 .. A height) {
        A[i, j] = generator next()
        B[i, j] = generator next()
    }

C = A * B
D = C inverse()
E = C * D

