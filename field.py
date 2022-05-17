from random import randint, choice

from cell import Cell


class Field:
    def __init__(self, random_fill=True):
        self.win = False
        self.count = 15
        self.field = Field.create_field()
        if random_fill:
            self.set_started()

    @staticmethod
    def create_field():
        field = []
        for i in range(9):
            line = [Cell(j, i) for j in range(9)]
            field.append(line)
        return field

    def __str__(self):
        stre = ''
        for i, line in enumerate(self):
            stre += ''.join(map(str, line[:3])) + ' '
            stre += ''.join(map(str, line[3:6])) + ' '
            stre += ''.join(map(str, line[6:9])) + '\n'
            if (i % 3) == 2:
                stre += '\n'
        return stre[:-1]

    def __len__(self):
        return len(self.field)

    def __getitem__(self, key):
        return self.field[key]

    def __iter__(self):
        return iter(self.field)

    @property
    def as_sectors(self):
        field = [[] for _ in range(9)]
        for i, line in enumerate(self):
            if i < 3:
                field[0] += line[0:3]
                field[1] += line[3:6]
                field[2] += line[6:9]
            elif i < 6:
                field[3] += line[0:3]
                field[4] += line[3:6]
                field[5] += line[6:9]
            else:
                field[6] += line[0:3]
                field[7] += line[3:6]
                field[8] += line[6:9]
            continue
        return field

    @property
    def rows(self):
        return self

    @property
    def cols(self):
        cols = []
        for j in range(len(self[0])):
            col = [self[i][j] for i in range(len(self))]
            cols.append(col)
        return cols

    def get_valid_values(self, sector, cell):
        invalid_values = set()
        for tcell in sector:
            invalid_values.add(tcell.value)
        for tcell in self.cols[cell.x]:
            invalid_values.add(tcell.value)
        for tcell in self.rows[cell.y]:
            invalid_values.add(tcell.value)
        valid_values = list(range(1, 10))
        for value in invalid_values:
            if value not in valid_values:
                continue
            index = valid_values.index(value)
            del valid_values[index]
        return valid_values

    def set_started(self):
        sectors = self.as_sectors
        created = True
        while self.count:
            id_sector = randint(0, 8)
            id_cell = randint(0, 8)
            sector = sectors[id_sector]
            cell = sector[id_cell]
            if cell.value != 0:
                continue
            self.count -= 1
            valid_values = self.get_valid_values(sector, cell)
            if not len(valid_values):
                created = False
                break
            cell.value = choice(valid_values)
        if not created:
            del self.field
            self.__init__()

    def get_filled(self):
        fill = []
        for line in self:
            fill.append([bool(cell.value) for cell in line])
        return fill

    def check_win(self):
        filled = self.get_filled()
        fill = all(all(line) for line in filled)
        self.win = fill
        return fill

    def get_sector_of_cell(self, cell):
        j, i = cell.pos
        j_sector = j // 3
        i_sector = i // 3
        id_sector = 3*i_sector + j_sector
        sectors = self.as_sectors
        print(id_sector, len(sectors))
        return sectors[id_sector]

    def set(self, row, col, value):
        i = row - 1
        j = col - 1
        cell = self[i][j]
        if value == 0:
            cell.value = value
            return

        sector = self.get_sector_of_cell(cell)
        valid_values = self.get_valid_values(sector, cell)
        if value in valid_values:
            self[i][j].value = value
            self.check_win()
            return
        return {'error': f'Invalid value ({value}) on cords ({i+1}, {j+1})'}
