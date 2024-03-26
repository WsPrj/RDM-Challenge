# RDM Mobility Challenge

#Sawruer Werner

'''Desarrollar una herramienta de gestión de stock de vehículos que permita a los usuarios validar y segmentar el inventario según dos tipos de contrato: "Renting" y "Fleet". La herramienta debe presentarse como una aplicación de consola, donde los usuarios puedan ingresar la cantidad de vehículos disponibles. Al finalizar la entrada de datos, la herramienta deberá proporcionar dos conjuntos de resultados claramente segmentados: uno para los vehículos bajo contrato de "Renting" y otro para aquellos bajo contrato de "Fleet". Estos resultados deben incluir la cantidad total de vehículos.'''

stockCont = 0
rentingCont = 0
fleetCont = 0


rentingCont = int(input('ingrese la cantidad de vehiculos bajo contrato de tipo Renting  '))
fleetCont = int(input('ingrese la cantidad de vehiculos bajo contrato tipo Fleet  '))
stockCont = rentingCont + fleetCont
print('')
print('La cantidad de Vehiculos es: ', stockCont)
print('------------------------------------------')
print('De los cuales ', rentingCont, ' Son con contrato tipo Renting')
print('Y ', fleetCont, ' son bajo contrato tipo Fleet')

def validar_stock():
    print('')
    print('La cantidad de Vehiculos es: ', stockCont)
    print('------------------------------------------')
    print('De los cuales ', rentingCont, ' Son con contrato tipo Renting')
    print('Y ', fleetCont, ' son bajo contrato tipo Fleet')
    print('')

validar = (input('si desea validar el stock bajo tipos de contratos presione "1" '))
if validar == '1':
    print('La cantidad total de vehiculos es: ', stockCont)
    print('------------------------------------------')
    print('De los cuales ', rentingCont, ' Son con contrato tipo Renting')
    print('Y ', fleetCont, ' son bajo contrato tipo Fleet')
    print('fin del programa')
else:
    print('fin del programa')
