command=''
signal=False
while True:
    command= input('> ').lower()
    if command == 'green':
        if signal:
            print('Signal is already green')
        else:
            print('Signal set to GREEN. Vehicles can move.')
            signal=True
    elif command == 'red':
        if not signal:
            print('Signal is already red')
        else:
            print('Signal set to RED. Vehicles must stop.')
            signal=False
    elif command == 'help':
        print('''green - Set signal to green
yellow - Set signal to yellow
red - Set signal to red
exit - Exit the program''')
    elif command=='exit':
        print('Exiting...')
        break
    else:
        print("Invalid command. Type 'help' for options.")

