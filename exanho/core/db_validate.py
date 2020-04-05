import concurrent.futures as f

def validate(has_db_model_configs):
    futures = set()
    results = []
    canceled = False
    with f.ProcessPoolExecutor(len(has_db_model_configs)) as executor:
        for config in has_db_model_configs:
            future = executor.submit(inner_validate, config['module'], config['url'])
            futures.add(future)

        try:
            for future in f.as_completed(futures):
                err = future.exception()
                if err is None:
                    result = future.result()
                    results.append(result)
                else:
                    raise err

        except KeyboardInterrupt:
            canceled = True
            for future in futures:
                future.cancel()
            executor.shutdown()

    return results, canceled

def inner_validate(module, url):
    import importlib
    mod = importlib.import_module(module)
    valid, errors, warnings = mod.domain.validate(url)
    return module, valid, errors, warnings