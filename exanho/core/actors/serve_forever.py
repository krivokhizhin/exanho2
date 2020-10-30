
from collections import namedtuple

ServeByProcess = namedtuple('ServeByProcess', ['process', 'serve'])

def serve_forever(serve, context, db_key, max_workers=0, **kwargs):

    if db_key:
        domain = context.get_domain(db_key)

        # Using Connection Pools with Multiprocessing or os.fork() , second approach:
        # https://docs.sqlalchemy.org/en/13/core/pooling.html#using-connection-pools-with-multiprocessing-or-os-fork
        domain.dispose()

        from exanho.orm.domain import Sessional
        Sessional.domain = domain

    if max_workers and isinstance(max_workers, int) and max_workers > 0:
        from threading import Thread
        for _ in range(max_workers):
            Thread(target=serve, daemon=True, kwargs=kwargs).start()

    serve(**kwargs)