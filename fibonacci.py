### Suseción de Fibonacci ###

def fibonacci():

    vec = list(range(0, 33))   
    vec[1] = 0
    vec[2] = 1

    for i in range(3,33):

        vec[i] = vec[i-1] + vec[i-2]
        print(vec[i])


fibonacci()



