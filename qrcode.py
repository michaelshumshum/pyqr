from requests import get
import sys
# OVERENGINEERED BASIC LOGGING


class Logger:

    class Severity:
        pass

    class Moderate(Severity):
        pass

    class Error(Severity):
        pass

    class Success(Severity):
        pass

    class Warn(Severity):
        pass

    @classmethod
    def log(cls, text, severity=Moderate):
        output = ''
        if not isinstance(severity(), cls.Severity):
            raise TypeError(f'must be Logger.Severity, not {severity.__name__}')
        if isinstance(severity(), cls.Moderate):
            output += '[INFO]'
        elif isinstance(severity(), cls.Error):
            output += '[31m[ERROR][0m'
        elif isinstance(severity(), cls.Success):
            output += '[32m[SUCCESS][0m'
        elif isinstance(severity(), cls.Warn):
            output += '[33m[WARN][0m'
        print(output + ' ' + text)


# ARGUMENT PARSING

options = {
    'data': None,
    'dimensions': '200x200',
    'encoding': 'utf-8',
    'directory': None,
    'filename': 'qr',
}

try:
    args = [(arg[1:], sys.argv[index + 1]) for index, arg in enumerate(sys.argv) if '-' in arg]
except IndexError:
    Logger.log(text='Invalid Arguments', severity=Logger.Error)
    sys.exit()

for option, value in args:
    if option not in options.keys():
        Logger.log(text=f'Ignoring option {option} with argument {value}', severity=Logger.Warn)
        continue
    options[option] = value

for option, value in options.items():
    Logger.log(text=f'Using {value} as {option}', severity=Logger.Moderate)

if any(value is None for key, value in options.items()):
    Logger.log(text='Missing required arguments', severity=Logger.Error)
    sys.exit()

try:
    with open(f'{options["directory"]}/{options["filename"]}.png', 'wb') as img:
        try:
            response = get(f'https://chart.googleapis.com/chart?cht=qr&chs={options["dimensions"]}&chl={options["data"].replace(", ", " % 20")}&choe={options["encoding"]}')
        except HTTPError:
            Logger.log(text='HTTP Error', severity=Logger.Error)
            sys.exit()
        if response.status_code == 400:
            Logger.log(text='Invalid Arguments', severity=Logger.Error)
            sys.exit()
        img.write(response.content)
        Logger.log(text=f'Saved {options["filename"]}.png to {options["directory"]}', severity=Logger.Success)
except FileNotFoundError:
    Logger.log(text='Invalid directory', severity=Logger.Error)

    'directory': None,
    'filename': 'qr',
}

try:
    args = [(arg[1:], sys.argv[index + 1]) for index, arg in enumerate(sys.argv) if '-' in arg]
except IndexError:
    logger.log(text='Invalid Arguments', severity=logger.Error)
    sys.exit()

for option, value in args:
    if option not in options.keys():
        logger.log(text=f'Ignoring option {option} with argument {value}', severity=logger.Warn)
        continue
    options[option] = value

for option, value in options.items():
    logger.log(text=f'Using {value} as {option}', severity=logger.Moderate)

if any(value is None for key, value in options.items()):
    logger.log(text='Missing required arguments', severity=logger.Error)
    sys.exit()

try:
    with open(f'{options["directory"]}/{options["filename"]}.png', 'wb') as img:
        try:
            response = get(f'https://chart.googleapis.com/chart?cht=qr&chs={options["dimensions"]}&chl={options["data"].replace(", ", " % 20")}&choe={options["encoding"]}')
        except HTTPError:
            logger.log(text='HTTP Error', severity=logger.Error)
            sys.exit()
        if response.status_code == 400:
            logger.log(text='Invalid Arguments', severity=logger.Error)
            sys.exit()
        img.write(response.content)
        logger.log(text=f'Saved {options["filename"]}.png to {options["directory"]}', severity=logger.Success)
except FileNotFoundError:
    logger.log(text='Invalid directory', severity=logger.Error)
