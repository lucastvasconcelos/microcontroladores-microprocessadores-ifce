def recebe_binario(x,lista_nome_binario):
    x = list(x)
    tamanho = len(x)
    lista_nome_binario.append("0x01,0x00")
    for i in range(0,tamanho):
        lista_nome_binario.append("0x0"+ x[(tamanho-1) - i])                                                     

    return (lista_nome_binario)


def converte(nome):
    nome = nome.upper()
    lista_nome = list(nome)
    final = "0x01,0x80"
    lista_nome_binario= []
    for letra in lista_nome:
        if letra == 'A':
            binario_a = '01000001'
            recebe_binario(binario_a,lista_nome_binario)                                       

        elif letra == 'B':
            binario_b = '01000010'
            recebe_binario(binario_b,lista_nome_binario)
        elif letra == 'C':
            binario_c = '01000011'            
            recebe_binario(binario_c,lista_nome_binario)
        elif letra == 'D':
            binario_d = '01000100' 
            recebe_binario(binario_d,lista_nome_binario)
        elif letra == 'E':
            binario_e = '01000101'     
            recebe_binario(binario_e,lista_nome_binario)
        elif letra == 'F':
            binario_f = '01000110' 
            recebe_binario(binario_f,lista_nome_binario)
        elif letra == 'G':
            binario_g = '01000111' 
            recebe_binario(binario_g,lista_nome_binario)
        elif letra == 'H':
            binario_h = '01001000' 
            recebe_binario(binario_h,lista_nome_binario)
        elif letra == 'I':
            binario_i = '01001001' 
            recebe_binario(binario_i,lista_nome_binario)
        elif letra == 'J':
            binario_j = '01001010' 
            recebe_binario(binario_j,lista_nome_binario)
        elif letra == 'K':
            binario_k = '01001011'               
            recebe_binario(binario_k,lista_nome_binario)
        elif letra == 'L':
            binario_l = '01001100' 
            recebe_binario(binario_l,lista_nome_binario)
        elif letra == 'M':
            binario_m = '01001101' 
            recebe_binario(binario_m,lista_nome_binario)
        elif letra == 'N':
            binario_n = '01001110' 
            recebe_binario(binario_n,lista_nome_binario)            
        elif letra == 'O':
            binario_o = '01001111' 
            recebe_binario(binario_o,lista_nome_binario)
        elif letra == 'P':
            binario_p = '01010000' 
            recebe_binario(binario_p,lista_nome_binario)
        elif letra == 'Q':
            binario_q = '01010001' 
            recebe_binario(binario_q,lista_nome_binario)
        elif letra == 'R':
            binario_r = '01010010' 
            recebe_binario(binario_r,lista_nome_binario)            
        elif letra == 'S':
            binario_s = '01010011' 
            recebe_binario(binario_s,lista_nome_binario)
        elif letra == 'T':
            binario_t = '01010100' 
            recebe_binario(binario_t,lista_nome_binario)
        elif letra == 'U':
            binario_u = '01010101' 
            recebe_binario(binario_u,lista_nome_binario)
        elif letra == 'V':
            binario_v = '01010110' 
            recebe_binario(binario_v,lista_nome_binario)
        elif letra == 'W':
            binario_w = '01010111' 
            recebe_binario(binario_w,lista_nome_binario)
        elif letra == 'X':
            binario_x = '01011000' 
            recebe_binario(binario_x,lista_nome_binario)
        elif letra == 'Y':
            binario_y = '01011001' 
            recebe_binario(binario_y,lista_nome_binario)
        elif letra == 'Z':
            binario_z = '01011010' 
            recebe_binario(binario_z,lista_nome_binario)
        elif letra == ' ':
            binario_space = '00100000'
            recebe_binario(binario_space,lista_nome_binario)
            
    lista_nome_binario.append(final)            

    lista_nome_binario = str(lista_nome_binario)
    lista_nome_binario = lista_nome_binario.replace("'","")
    lista_nome_binario = lista_nome_binario.replace("[","")
    lista_nome_binario = lista_nome_binario.replace("]","")
    arquivo = open("seu_nome.ptn","w")

    arquivo.write(lista_nome_binario)    
    arquivo.close()


    print(lista_nome_binario)

nome_usuario = input("Digite seu nome: ")
converte(nome_usuario)
