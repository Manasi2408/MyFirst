# raining code

rain = ''
while not rain:
    #or while rain != 'no':
    print("Is it raining ?")
    answer = input()
    if answer == 'yes':
        print('Do you have an umbrella ?')
        umbrella = input()
        if umbrella == 'yes':
            print("Take the umbrella .")
            break
        else:
            print("Wait outside .")
    else:
        print('Go outside .')

# # # # End of code # # #