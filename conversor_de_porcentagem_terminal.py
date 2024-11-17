print("Conversor de porcentagem em páginas lidas")

total_de_paginas = int(input('Coloque o total de páginas:  '))
porcentagem = int(input('Coloque a porcentagem lida:  '))

paginas_lidas = (total_de_paginas / 100)  * porcentagem

print('Ate agora eu li {:.0f} paginas'.format(paginas_lidas))
