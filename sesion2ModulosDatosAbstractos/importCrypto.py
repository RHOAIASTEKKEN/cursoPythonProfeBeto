import hashlib

print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_available))))