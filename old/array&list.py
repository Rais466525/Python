# List = array
UwU = ['Islam', 'Rais', 'Andrey', 'Dima', 'Mura']

print('\n\033[1m----index 0 \033[0m')
print(UwU[0])

print('\n\033[1m----get last index \033[0m')
print(UwU[-1])

print('\n\033[1m----add to array Haly \033[0m')
UwU.append('Haly')
print(UwU)

print('\n\033[1m----delate Andrey from array \033[0m')
UwU.remove('Andrey')
print(UwU)

print('\n\033[1m----map the array \033[0m')
for nol in UwU:
    print(nol)

print('\n\033[1m----test isRais in the array \033[0m')
if 'Rais' in UwU:
    print('Yes')
else:
    print('No')

print('\n\033[1m----map with index \033[0m')
print(UwU[1:3])

print('\n\033[1m----metod reverse \033[0m')
UwU.reverse
print(UwU)

print('\n\033[1m----SORT \033[0m')
sortedUwU = sorted(UwU)
print(sortedUwU)