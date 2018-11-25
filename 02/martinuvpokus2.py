from random import choice

var = ('kámen', 'nůžky', 'papír')

volba_pocitace = choice(var)
print('Zvolte kámen, nůžky, nebo papír: ')
volba_cloveka = input()

print('Člověk zvolil {} a počítač zvolil {}'.format(volba_cloveka, volba_pocitace))

if volba_pocitace == volba_cloveka:
    print('plichta')
elif (volba_pocitace == 'kámen' and volba_cloveka == 'nůžky') \
  or (volba_pocitace == 'papír' and volba_cloveka == 'kámen') \
  or (volba_pocitace == 'nůžky' and volba_cloveka == 'papír'):
    print('Vyhrává počítač.')
elif (volba_cloveka == 'kámen' and volba_pocitace == 'nůžky') \
  or (volba_cloveka == 'papír' and volba_pocitace == 'kámen') \
  or (volba_cloveka == 'nůžky' and volba_pocitace == 'papír'):
    print('Vyhrává člověk!')
else:
    print('Člověk nedal správné zadání.')

