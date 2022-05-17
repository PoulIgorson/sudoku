import os

from field import Field


def check_input(args):
    if len(args) != 3:
        return {'error': 'Enter three value'}
    try:
        row, col, value = map(int, args)
    except ValueError:
        return {'error': 'Enter numbers'}
    if not ((1 <= row <= 9) and (1 <= col <= 9) and (1 <= value <= 9)):
        return {'error': 'Enter valid values:\n\t(1 <= row <= 8),\n\t(1 <= col <= 8),\n\t(1 <= value <= 9)'}
    return {'args': (row, col, value)}


def check_cmd(args):
    resp = {}
    if 'quit' in args or 'exit' in args:
        resp['run'] = False
    return resp


def setfield(field):
    sectors = field.as_sectors
    sectors[0][0].value = 2
    sectors[0][2].value = 8
    sectors[0][3].value = 4
    sectors[0][5].value = 9
    sectors[0][7].value = 7
    sectors[0][8].value = 3
    
    sectors[1][0].value = 9
    sectors[1][1].value = 3
    sectors[1][2].value = 6
    sectors[1][5].value = 1
    sectors[1][6].value = 4
    sectors[1][7].value = 8
    sectors[1][8].value = 2
    
    sectors[2][2].value = 5
    sectors[2][3].value = 3
    sectors[2][4].value = 8
    sectors[2][5].value = 2
    sectors[2][6].value = 1
    sectors[2][7].value = 6
    
    sectors[3][1].value = 5
    sectors[3][2].value = 7
    sectors[3][4].value = 9
    sectors[3][5].value = 4
    sectors[3][7].value = 3
    
    sectors[4][0].value = 2
    sectors[4][1].value = 9
    sectors[4][3].value = 6
    sectors[4][5].value = 3
    sectors[4][6].value = 7
    sectors[4][8].value = 5
    
    sectors[5][0].value = 6
    sectors[5][2].value = 4
    sectors[5][3].value = 5
    sectors[5][4].value = 2
    sectors[5][6].value = 9
    sectors[5][7].value = 1
    sectors[5][8].value = 8
    
    sectors[6][0].value = 3
    sectors[6][2].value = 1
    sectors[6][3].value = 9
    sectors[6][4].value = 4
    sectors[6][6].value = 7
    sectors[6][7].value = 8
    sectors[6][8].value = 5
    
    sectors[7][1].value = 5
    sectors[7][2].value = 9
    sectors[7][4].value = 2
    sectors[7][6].value = 1
    sectors[7][8].value = 4
    
    sectors[8][1].value = 7
    sectors[8][2].value = 6
    sectors[8][4].value = 5
    sectors[8][5].value = 1
    sectors[8][6].value = 2
    sectors[8][8].value = 3


def main():
    field = Field(random_fill=False)
    setfield(field)
    error = ''
    run = True
    while run:
        os.system('cls')
        print(field, end='\n\n')
        if error:
            print('ERROR:')
            print(error, '\n')
            error = ''
        if field.win:
            print('You WIN!!!')
            run = False
            continue
        args = input(f'Enter (row col value): ').split()
        resp = check_cmd(args)
        if 'run' in resp.keys():
            run = resp['run']
        resp = check_input(args)
        if 'error' in resp.keys():
            error = resp['error']
            continue
        resp = field.set(*resp['args'])
        if isinstance(resp, dict) and 'error' in resp.keys():
            error = resp['error']


if __name__ == '__main__':
    main()
