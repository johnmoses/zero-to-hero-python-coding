# Exceptions

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

## Blocks in exception statement

- The try block lets you test a block of code for errors.
- The except block lets you handle the error.
- The else block lets you execute code when there is no error.
- The finally block lets you execute code, regardless of the result of the try- and except blocks.

## Logging

Logging is the production-grade alternative to `print()` for tracking events and errors in your application.

```py
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('Debug detail')
logging.info('Process started')
logging.warning('Low disk space')
logging.error('File not found')
logging.critical('System failure')
```

### Log levels (low → high)

`DEBUG` → `INFO` → `WARNING` → `ERROR` → `CRITICAL`

Set the level to control which messages appear. In production, use `WARNING` or above.
