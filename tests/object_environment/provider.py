import hashlib


class Provider:

    _counter = 0
    _ean = 1000000000000

    def kwargs(self, default, kw):
        default.update(kw)
        return default

    def unique_text(self, max_length=35):
        self._counter += 1
        hashed = hashlib.md5(
            str(self._counter).encode()
        ).hexdigest()

        return (str(self._counter) + str(hashed))[:max_length]

    def unique_number(self, length=None):
        self._counter += 1
        if length:
            counter_length = len(str(self._counter))
            loop_range = int(length) - counter_length
            if not loop_range >= 0:
                raise ValueError('Number already used')    
            else:
                number = ''
                for i in range(loop_range):
                    number += '0'
                return str(self._counter) + number 
        else:
            return self._counter

    def unique_ean(self):
        self._ean += 1
        return str(self._ean)
