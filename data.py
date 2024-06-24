from datetime import datetime

dataAtual = datetime.now()

dataConvertida = dataAtual.strftime('%Y-%m-%d')
horaAtual = dataAtual.strftime('%H:%M:%S')

print('Data Atual:', dataConvertida)
print('Hora Atual', horaAtual)
