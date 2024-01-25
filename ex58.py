import random

print('-=-' * 20);
print('O npc pensara em um número entre 0 e 10, tente adivinhar!');
print('-=-' * 20);

user = int(input('Que número o npc pensou? '));
ncp = random.randint(0,10);
cont = 0;

while user != ncp:
  cont += 1
  if user < ncp:
    print('É maior...');
    user = int(input('Tente novamente! '));
  else:
    print('É menor...');
    user = int(input('Tente novamente! '));
print(f'\nParabéns você levou {cont} rodadas para acertar!\nEra o número {ncp}.');

