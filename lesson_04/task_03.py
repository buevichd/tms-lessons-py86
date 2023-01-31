is_moving = input('Is it moving? ')
should_move = input('Should it move? ')
if is_moving == 'yes' and should_move == 'no':
    print('Use glue')
elif is_moving == 'no' and should_move == 'yes':
    print('Use oil')
else:
    print("Don't touch")
