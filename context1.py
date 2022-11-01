# Context manager using function 

from contextlib import contextmanager


@contextmanager
def open_file(file,mode):
    f = open (file,mode)
    yield f
    f.close()

with open_file('file.txt', 'w') as f:
    f.write('my name is jyothsna')

print(f.closed)
