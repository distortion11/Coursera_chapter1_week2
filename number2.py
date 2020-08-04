from scipy import linalg as lin
import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    print("Значение функции в точках 1 4 10 15")
    print(np.sin(1 / 5) * np.exp(1 / 10) + 5 * (np.exp(-1 * 1 / 2)))
    print(np.sin(4 / 5) * np.exp(4 / 10) + 5 * (np.exp(-1 * 4 / 2)))
    print(np.sin(10 / 5) * np.exp(10 / 10) + 5 * (np.exp(-1 * 10 / 2)))
    print(np.sin(15 / 5) * np.exp(15 / 10) + 5 * (np.exp(-1 * 15 / 2)))
    A  = np.array([[1,1],[1,14]])
    B  = np.array([3.252,0.635])
    w = lin.solve(A, B, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, debug=False,
                       check_finite=True)
    x = np.arange(1,15,0.1)
    y = np.sin(x/5)*np.exp(x/10) + 5*(np.exp(-1*x/2))
    y_solve = w[0] + x*w[1]
    plt.plot(x,y,'r',label = 'F(x)')
    plt.grid()
    plt.plot(x,y_solve,'b',label = 'polinom 1')

    A1 = ([[1,1,1,1],[1,4,16,64],[1,10,100,1000],[1,15,225,3375]])
    B1 = ([3.252,1.74,2.505,0.635])


    answer =   lin.solve(A1, B1, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, debug=False,
                       check_finite=True)
    print(answer)
    y_answer = answer[0] + x * answer[1] + x**2*answer[2]+x**3*answer[3]
    plt.plot(x, y_answer, 'y',label = 'polinom 3')
    plt.legend()
    plt.show()
    answerr = ''
    for elem in answer:
        answerr = answerr + str(round(elem,2)) + " "
    filename = open('submission-2.txt', 'w')
    filename.write(answerr)
    filename.close()
    print(answerr)