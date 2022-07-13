import numpy as np
from math import log

class Base():
    
    def __init__(self, base: int, *, symbols: np.ndarray = None) -> None:
        self.base  = base
        
        if symbols == None:
            sym = [i for i in range(10)]
            sym += [chr(i) for i in range(65, 91)]
            symbols = np.array(sym, dtype=str)
        self.symbols = symbols
        
        self.symbols_dic = {}
        for i, s in enumerate(self.symbols):
            self.symbols_dic[s] = i
        
        if self.base > len(self.symbols):
            raise ValueError(f"Not enough symbols (number of symbols: {len(self.symbols)}) for the base {self.base}")
    
    def _factor(self, v: float) -> tuple:
        order = int(np.floor(log(v, self.base)))
        orders = range(0, order+1)[::-1]
        
        digits = np.empty((order+1), dtype=int)
        for place in orders:
            digit = int(np.floor(v / self.base**place))
            digits[place] = digit
            v = v % (self.base**place)
        
        return digits, orders
    
    def value_to_base(self, v: float) -> str:
        digits, orders = self._factor(v)
        return "".join([self.symbols[digits[i]] for i in orders])
    
    def value_from_base(self, v: str) -> float:
        num = 0
        for i, letter in enumerate(v):
            num += self.base**(len(v)-i-1)*self.symbols_dic[letter]
        return num
    
    def convert_base(self, v: str, to_base) -> str:
        num = self.value_from_base(v)
        return to_base.value_to_base(num)

if __name__ == "__main__":
    b16 = Base(16)
    txt1 = b16.value_to_base(7842)
    print(txt1)
    b2 = Base(2)
    txt2 = b16.convert_base(txt1, b2)
    print(txt2)
    val = b2.value_from_base(txt2)
    print(val)