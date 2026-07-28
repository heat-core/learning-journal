class Strint(int):
    
    def __lt__(self, other):
        return abs(self) % 10 < abs(other) % 10

    def __gt__(self, other):
        return abs(self) % 10 > abs(other) % 10

    def __le__(self, other):
        return abs(self) % 10 <= abs(other) % 10

    def __ge__(self, other):
        return abs(self) % 10 >= abs(other) % 10

    def __eq__(self, other):
        return abs(self) % 10 == abs(other) % 10

    def __ne__(self, other):
        return abs(self) % 10 != abs(other) % 10

    def __add__(self, other):
        res_str = str(self) + str(other)
        return Strint(res_str)


    def __sub__(self, other):
        s1 = str(self)
        s2 = str(other)
        if not s1.endswith(s2):
            raise ValueError('The subtraction is not valid!')
        res_str = s1[:-len(s2)]
        if res_str == "":
            return Strint(0)
        else:
            return Strint(res_str)


    def __len__(self):
        return len(str(self))


    def __call__(self):
        fa_digits = {
            '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
            '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
        }
        return ''.join(fa_digits[digit] for digit in str(self))
