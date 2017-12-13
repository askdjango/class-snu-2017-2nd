

def main(number):
    print('number : {}'.format(number))
    print()

    for i in range(1, number+1):
        blank = (number-i) * ' '
        star = (i*2-1) * '*'
        print(blank, star, sep='')

    for i in range(number-1, 0, -1):
        blank = (number-i) * ' '
        star = (i*2-1) * '-'
        if len(star) > 2:
            star = '|' + star[1:-1] + '|'
        else:
            star = '|'
        print(blank, star, sep='')


if __name__ == '__main__':
    main(1)
    main(2)
    main(3)
    main(5)
    main(7)
    main(20)
    main(40)

