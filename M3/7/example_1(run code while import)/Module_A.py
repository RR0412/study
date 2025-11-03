class Storage:
    counter = 0

def action():
    Storage.counter += 1
    print(f'Action from module A changes state of the Storage. Counter is : {Storage.counter}')

if __name__ == '__main__':  # у главного модуля __name__ всегда "__main__"
    action()
