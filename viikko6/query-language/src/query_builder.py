from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query=None):
        self._query = query

    def build(self):
        return self._query

    def all(self):
        if self._query != None:
            return QueryBuilder(And(self._query, All()))
        return QueryBuilder(All())

    def playsIn(self, team):
        if self._query != None:
            return QueryBuilder(And(self._query, PlaysIn(team)))
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        if self._query != None:
            return QueryBuilder(And(self._query, HasAtLeast(value, attr)))
        return QueryBuilder(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        if self._query != None:
            return QueryBuilder(And(self._query, HasFewerThan(value, attr)))
        return QueryBuilder(And(HasFewerThan(value, attr)))

    def oneOf(self, *attr):
        return QueryBuilder(Or(*attr))