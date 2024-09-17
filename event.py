import g


# Get log...
def get(arg=None):
    return g.pg.event.get(arg)
