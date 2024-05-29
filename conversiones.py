import sys
print(f"______********CASA   DE   CAMBIO*********______\
        \nMoneda extranjera          Equivalencia CL\
        \nSol    :  Tasa= {sys.argv[1]}     CL$ {float(sys.argv[1])*int(sys.argv[4])}\
        \nPesoArg:  Tasa= {sys.argv[2]}     CL$ {float(sys.argv[2])*int(sys.argv[4])}\
        \nUSDolar:  Tasa= {sys.argv[3]}     CL$ {float(sys.argv[1])*int(sys.argv[4])}\
        \n ------------------------------------------------")
        