
def piramida():
    data=int(input('Ingrese un numero para graficar \n'))
    imp=data%2

    if(imp!=0):
            try:
              arch=open('piramide.txt','w')

              for a in range(1,data+1):
                    i = 0
                    while i<a:
                        arch.write('#')
                        print('#', end='')
                        i+=1
                    a+=1
                    print(' ')
                    arch.write('\n')
              u = data-1
              while u>=0:
                     i = 0
                     while i < u:
                         arch.write('#')
                         print('a',end='')
                         i+=1
                     u-=1
                     print(' ')
                     arch.write('\n')
              arch.close()
              print('piramide generada att: 201900952')
            except:
                print('hubo un error!')
                exit()
    else:
     print('Numero debe ser impar! \n')
    exit()


piramida()