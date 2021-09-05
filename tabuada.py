from termcolor import colored
print(colored('-=-'*20,'yellow'))
print(colored('Tabuada','green'))
print(colored('-=-'*20,'yellow'))
nu = int(input('Qual o valor da tabuada que você quer?'))
a = 0
while (a < 10):
    print('{} x {} = {}'.format(a,nu, a*nu))
    a= a + 1
else:
    print('{} x {} = {}'.format(10,nu,10*nu))