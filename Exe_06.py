def number_test():

    while True:
        number = input('Enter Your Number:')
        CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
        CN_union = [130,131,132,155,156,185,186,145,176,1709]
        CN_telecom = [133,153,180,181,189,177,1700]
        first_three = int(number[0:3])
        first_four = int(number[0:4])

        if len(number) == 11:

            if first_three in CN_mobile or first_four in CN_mobile:
                print('Operator:China Mobile')
                print('We\'re sending verification code via text to your phone:',number)
                break
            elif first_three in CN_telecom:
                print('Operator : China Telecom')
                print('We\'re sending verification code via text to your phone:',number)
                break
            elif first_three in CN_union:
                print('Operator:China Union')
                print('We\'re sending verification code via text to your phone:',number)
                break
            else:
                print('No such a operator')
        else:
            print('Invalid length,your number should be in 11 digits')

number_test()
