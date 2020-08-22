def read_matrix(dim2):
    n2 = int(dim2[0])
    m2 = int(dim2[1])
    b = []
    for i in range(n2):
        x = input().split(" ")
        for j in range(m2):
            b.append(x[j])
    return b


def mult_num(dim, c, mat1):
    i = 0
    while i < int(dim[0]) * int(dim[1]):
        z = float(c) * float(mat1[i])
        if mat1[0].isdigit() and c.isdigit():
            z = int(z)
        else:
            z = float(z)
        if (i + 1) % int(dim[1]) != 0:
            print(z, end=" ")
        else:
            print(z, end="\n")
        i += 1


def add_matrix(dim1, mat1, mat2):
    i = 0
    while i < int(dim1[0]) * int(dim1[1]):
        z = float(mat1[i]) + float(mat2[i])
        if mat1[0].isdigit() and mat2[0].isdigit():
            z = int(z)
        else:
            z = float(z)
        if (i + 1) % int(dim1[1]) != 0:
            print(z, end=" ")
        else:
            print(z, end="\n")
        i += 1


def mult_matrix(dim1, dim2, mat1, mat2):
    a = int(dim1[0])
    b = int(dim2[1])
    d = int(dim2[0])
    for i in range(0, a * b, 1):
        z = 0
        c = i // b

        for j in range(0, d, 1):
            z += float(mat1[c * d + j]) * float(mat2[j * b + i % b])
        
        if mat1[0].isdigit() and mat2[0].isdigit():
            z = int(z)
        else:
            z = float(z)
        if (i + 1) % b != 0:
            print(z, end=" ")
        else:
            print(z, end="\n")


def determinant(dim, n):
    if n == 1:
        return dim[0][0]
    elif n == 2:
        return dim[0][0] * dim[1][1] - dim[0][1] * dim[1][0]
    else:
        det = 0
        for i in range(0, n):
            c = (-1) ** (i + 0) * dim[0][i]
            minor = []
            for j in range(1, n):
                m = []
                for y in range(0, n):
                    if y != i:
                        m.append(dim[j][y])
                minor.append(m)
            det += c * determinant(minor, n - 1)
           
        return det
 
 
def invert(dim, n):
    inv = []
    d = determinant(dim, n)
    for i in range(0, n):
        for j in range(0, n):
            minor = []
            for i1 in range(0, n):
                m = []
                if i1 != i:
                    for j1 in range(0, n):
                        if j1 != j:
                            m.append(dim[j1][i1])
                    minor.append(m)
            
            inv.append((-1) ** (i + j) * determinant(minor, n - 1) / d)
    for z in range(0, n ** 2):
        if (z + 1) % n != 0:
            print('%.4f' % inv[z], end=" ")
        else:
            print('%.4f' % inv[z], end="\n")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    a = int(input('Your choice:'))

    if a == 1:

        dim1 = input('Enter size of first matrix:').split(" ")
        print('Enter first matrix:')
        mat1 = read_matrix(dim1)

        dim2 = input('Enter size of second matrix:').split(" ")
        print('Enter second matrix:')
        mat2 = read_matrix(dim2)

        if int(dim1[0]) != int(dim2[0]) or int(dim1[1]) != int(dim2[1]):
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            add_matrix(dim1, mat1, mat2)
            print()

    elif a == 2:
        dim1 = input('Enter size matrix:').split(" ")
        print('Enter matrix:')
        mat1 = read_matrix(dim1)
        c = input('Enter constant:')
        print('The result is:')
        mult_num(dim1, c, mat1)
        print()

    elif a == 3:
        dim1 = input('Enter size of first matrix:').split(" ")
        print('Enter first matrix:')
        mat1 = read_matrix(dim1)

        dim2 = input('Enter size of second matrix:').split(" ")
        print('Enter second matrix:')
        mat2 = read_matrix(dim2)

        if int(dim1[1]) != int(dim2[0]):
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            mult_matrix(dim1, dim2, mat1, mat2)
        print()
        
    elif a == 5:
        dim1 = input('Enter size matrix:').split(" ")
        print('Enter matrix:')
        mat1 = []
        for _ in range(int(dim1[1])):
            mat1.append([int(x) if x.isdigit() else float(x) for x in input().split(" ")])   
        
        if int(dim1[1]) != int(dim1[0]):
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            print(determinant(mat1, int(dim1[0])))
        print()
    
    
    elif a == 6:
        dim1 = input('Enter size matrix:').split(" ")
        print('Enter matrix:')
        mat1 = []
        for _ in range(int(dim1[1])):
            mat1.append([int(x) if x.isdigit() else float(x) for x in input().split(" ")])   
        
        if int(dim1[1]) != int(dim1[0]) or determinant(mat1, int(dim1[0])) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print('The result is:')
            invert(mat1, int(dim1[0]))
        print()       
    
    elif a == 4:
        print()
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        e = int(input('Your choice:'))
        
        dim1 = input('Enter size matrix:').split(" ")
        print('Enter matrix:')
        mat1 = []
        for _ in range(int(dim1[1])):
            mat1.append([x for x in input().split(" ")])    

        if e == 1:
            for i in range(int(dim1[0])):
                for j in range(int(dim1[1])):
                    if mat1[j][i].isdigit():
                        print(int(mat1[j][i]), end=" ")    
                    else:
                        print(float(mat1[j][i]), end=" ")        
                print('\n')    
       
        elif e == 2:  
            i = int(dim1[0])
            while i > 0:
                j = int(dim1[1])
                while j > 0:
                    if mat1[j - 1][i - 1].isdigit():
                        print(int(mat1[j - 1][i - 1]), end=" ")
                    else:
                        print(float(mat1[j - 1][i - 1]), end=" ")     
                    j -= 1   
                print('\n')
                i -= 1   
        
        elif e == 3:   
            i = 0
            while i < int(dim1[0]):
                j = int(dim1[1])
                while j > 0:
                    if mat1[i][j - 1].isdigit():
                        print(int(mat1[i][j - 1]), end=" ")
                    else:
                        print(float(mat1[i][j - 1]), end=" ")     
                    j -= 1   
                print('\n')
                i += 1    
        
        elif e == 4:
            i = int(dim1[0])
            while i > 0:
                j = 0
                while j < int(dim1[1]):
                    if mat1[i - 1][j].isdigit():
                        print(int(mat1[i - 1][j]), end=" ")
                    else:
                        print(float(mat1[i - 1][j]), end=" ")     
                    j += 1   
                print('\n')
                i -= 1    
                 
             
    elif a == 0:
        break
