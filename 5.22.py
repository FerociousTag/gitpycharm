#Zachary Blackwell 1941472
print('Davy\'s auto shop services')
services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax' : 12,
    '-': 0
}
print('Oil change --', '${}'.format(services['Oil change']))
print('Tire rotation --', '${}'.format(services['Tire rotation']))
print('Car wash --', '${}'.format(services['Car wash']))
print('Car wax --', '${}'.format(services['Car wax']))
print()

first_service = input('Select first service:\n')
second_service = input('Select second service:\n')
print()

#invoice
print('Davy\'s auto shop invoice\n')
if first_service == '-':
    print('Service 1:', 'No service')
else:
    print('Service 1:', first_service + ',', '${}'.format(services[first_service]))
if second_service == '-':
    print('Service 2:', 'No service')
else:
    print('Service 2:', second_service + ',', '${}'.format(services[second_service]))
print()
print('Total:', '${}'.format(services[first_service] + services[second_service]))