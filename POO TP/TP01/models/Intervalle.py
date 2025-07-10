class Intervalle:
    def __init__(self, borne_inf, borne_sup):
        self._borne_inf = borne_inf
        self._borne_sup = borne_sup

    def __str__(self):
        return f"[ {self._borne_inf} ; {self._borne_sup} ]"

    @property
    def borne_inf(self):
        return self._borne_inf

    @borne_inf.setter
    def borne_inf(self, borne_inf):
        if borne_inf < self.borne_sup:
            self._borne_inf = borne_inf
        else: raise Exception("Sorry, no numbers below zero")

    @property
    def borne_sup(self):
        return self._borne_inf

    @borne_sup.setter
    def borne_sup(self, borne_sup):
        if borne_sup > self.borne_inf:
            self.borne_sup = borne_sup
        else: raise Exception("Sorry, no numbers below zero")

    def __add__(self, other):
        borne_inf = self._borne_inf + other._borne_inf
        borne_sup = self._borne_sup + other._borne_sup
        return Intervalle(borne_inf, borne_sup)

    def intersection(self, other):
        min_common = max(self._borne_inf, other._borne_inf)
        max_common = min(self._borne_sup, other._borne_sup)
        if min_common <= max_common:
            return Intervalle(min_common, max_common)
        else:
            return None

        # Union d'intervalles (uniquement si intersection non vide)

    def union(self, other):
        inter = self.intersection(other)
        if inter is None:
            return None
        min_union = min(self._borne_inf, other._borne_inf)
        max_union = max(self._borne_sup, other._borne_sup)
        return Intervalle(min_union, max_union)


i = Intervalle(1, 2)
print(i)
a = Intervalle(4, 98)

print(i.__add__(a))