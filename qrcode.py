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

    def log(self, text, severity=Moderate):
        output = ''
        if not isinstance(severity(), self.Severity):
            raise TypeError(f'must be Logger.Severity, not {severity.__name__}')
        if isinstance(severity(), self.Moderate):
            output += '[INFO]'
        elif isinstance(severity(), self.Error):
            output += '\u001b[31m[ERROR]\u001b[0m'
        elif isinstance(severity(), self.Success):
            output += '\u001b[32m[SUCCESS]\u001b[0m'
        elif isinstance(severity(), self.Warn):
            output += '\u001b[33m[WARN]\u001b[0m'
        print(output + ' ' + text)


logger = Logger()

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
