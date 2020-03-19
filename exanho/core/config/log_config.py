logconfig = {
    'version' : 1,
    'formatters' : {
        'main' : {
            'format' : '%(asctime)s %(levelname)-8s %(processName)-10s %(name)s %(message)s'
        }
    },
    'handlers' : {
        'file' : {
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter' : 'main',
            'filename' : 'rosmet.log',
            'maxBytes' : 5*1024*1024,
            'backupCount' : 10
        },
        'console' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'main',
            'level' : 'DEBUG',
            'stream' : 'ext://sys.stdout'
        },
        'zmq' : {
            'class' : 'rosmet.core.config.zmq_log_handler.ZeroMQSocketHandler',
            'formatter' : 'main',
            'level' : 'DEBUG',
            'uri' : 'tcp://*:5556'
        },
        'null' : {
            'class' : 'logging.NullHandler',
            'formatter' : 'main',
            'level' : 'DEBUG'
        }
    },
    'loggers' : {
        'rosmet' : {
            'level' : 'DEBUG',
            'handlers' : ['console', 'file', 'zmq'],
            'qualname' : 'rosmet',
            'propagate' : 0
        },
        'root' : {
            'level' : 'DEBUG',
            'handlers' : ['null']
        }
    }
}