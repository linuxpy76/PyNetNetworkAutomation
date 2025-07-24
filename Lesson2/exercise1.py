base = "192.168.254."
prefix = int(input("Enter CIDR notation prefix (25-30): "))

binary_prefix = f'{prefix:08b}'
binary_prefix_list = [int(digit) for digit in str(binary_prefix)]

print(binary_prefix)
print(binary_prefix_list)

binary_subnet_mask = []
binary_length = 32
for i in range(prefix):
    binary_subnet_mask.append(int(1))
for i in range(32 - len(binary_subnet_mask)):
    binary_subnet_mask.append(int(0))

eight_bit_mask_list = [str(num) for num in binary_subnet_mask[24:]]
eight_bit_mask_int = int(''.join(eight_bit_mask_list))



print(eight_bit_mask_int)
print(binary_subnet_mask[24:])
print(binary_subnet_mask)
print(len(binary_subnet_mask))