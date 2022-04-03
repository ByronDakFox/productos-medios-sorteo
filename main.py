# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#metodo de Algoritmo de productos medios
def  generarNumeros(min1, max1, cant,numCant):

    Min = int(min1);
    Max = int(max1);
    Min1 = str(min1);
    Max1 = str(max1);
    Cant= int(cant);
    numCant1 = int(numCant);
    count = 0;
    resp=[];

    xmin=min(Min,Max);
    xmax=max(Min,Max);

    if len(Min1) > 3 and len(Max1) > 3:
        tmp = xmin * xmax;
        for i in range(Cant):

            y0 = xmin * xmax;
            snum2 = str(y0);
            cant = len(snum2);

            if cant == 8:
                n = snum2[2:6];
                n1 = int(n) / 10000;
            elif (cant == 6):
                n = snum2[1:5];
                n1 = int(n) / 10000;
            else:
                n = snum2[1:5];
                n1 = int(n) / 10000;

            result = "y[{}]= {}".format(i+1, snum2);
            result1 = "x[{}]= {}".format(i+1, n);
            result2 = "r= {}".format(n1);
            resp.append(n);
            #salida = result + "||" + result1 + "||" + result2;
            #print(salida);
            if (count >= 1 and y0 == tmp):
                break;
            else:
                xmin = xmax;
                xmax = int(n);
            count = count + 1;
            numres=sorted(resp);
        print("Números del sorteo son :\n"+
              "***************** Sorteo PUCE ******************* \n"
              +str(numres)+"\n*************************************************");
        sopr=[];
        for y in range(numCant1):
            canNum=random.randint(0, len(numres));
            sopr.append(numres[canNum]);

        for z in sopr:
            mensaje=str(sopr);

        print("Los números ganadores son:\n" + mensaje);

    else:
        print("Error las semillas tiene que se mayor a 3");

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Gran Sorteo PUCE 2021');

    resp="S";
    while resp.upper()!="N":
        print('Ingrese sus números');
        max1 = input("Ingrese num1: ");
        min1 = input("Ingrese num2: ");
        cant = input("Ingrese la cantidad: ");
        numCant = input("Ingrese la cantidad de números ganadores: ");

        print("****************************");
        generarNumeros(min1, max1, cant, numCant);
        resp=input("Desea continuar S/N: ");
    print("Fin del programa");


