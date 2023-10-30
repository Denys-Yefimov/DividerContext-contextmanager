from contextlib import contextmanager


@contextmanager
def dividercontext(symbol):
    print(10*symbol)
    yield
    print(10*symbol)

a = input()
with dividercontext(a):
    print("Hallo, how are you?")
