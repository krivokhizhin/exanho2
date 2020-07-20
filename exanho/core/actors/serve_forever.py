def serve_forever(server, service, db_key, max_workers=0):

    if db_key:
        domain = service.context.get_domain(db_key)

        # Using Connection Pools with Multiprocessing or os.fork() , second approach:
        # https://docs.sqlalchemy.org/en/13/core/pooling.html#using-connection-pools-with-multiprocessing-or-os-fork
        domain.dispose()

        from exanho.orm.sqlalchemy import Sessional
        Sessional.domain = domain

    if max_workers and isinstance(max_workers, int):
        from threading import Thread
        for _ in range(max_workers):
            Thread(target=server.serve_forever, daemon=True).start()

    server.serve_forever()