from Module_A import Storage, action

print(f'Expecting Storage.counter to be 0. Storage.counter is : {Storage.counter}')
print('Calling  action from module B')
action()
print(f'Expecting Storage.counter to be 1. Storage.counter is : {Storage.counter}')
