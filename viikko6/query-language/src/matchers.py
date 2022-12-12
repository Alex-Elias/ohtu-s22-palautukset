class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return False
        
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False

class All:
    def matches(self, player):
        return player

class PlaysIn:
    def __init__(self, team, query=All):
        self.query = query
        self._team = team

    def matches(self, player):
        if(self.query.matches(player)):

            return player.team == self._team
        return False

class HasAtLeast:
    def __init__(self, value, attr, query=All):
        self._value = value
        self._attr = attr
        self.query = query

    def matches(self, player):
        if(self.query.matches(player)):
            player_value = getattr(player, self._attr)

            return player_value >= self._value
        return False

class HasFewerThan:
    def __init__(self, value, attr, query=All):
        self._value = value
        self._attr = attr
        self.query = query

    def matches(self, player):
        if(self.query.matches(player)):
            player_value = getattr(player, self._attr)

            return player_value < self._value
        return False


class QueryBuilder:
    def __init__(self, query = All()) -> None:
        self.query_object = query
    
    def build(self):
        return self.query_object
    
    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))
    
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team, self.query_object))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr, self.query_object))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr, self.query_object))
    
    
