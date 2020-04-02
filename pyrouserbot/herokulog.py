import datetime
import logging.handlers
import os


def setup(logdir='log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logdir = os.path.normpath(logdir)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    t = datetime.datetime.now()
    logfile = '{year:04d}{mon:02d}{day:02d}-' \
        '{hour:02d}{min:02d}{sec:02d}.log'.format(
            year=t.year, mon=t.month, day=t.day, 
            hour=t.hour, min=t.minute, sec=t.second)
    logfile = os.path.join(logdir, logfile)
    # 5mb logfile
    filehandler = logging.handlers.RotatingFileHandler(
        filename=logfile,
        maxBytes=5*1024*1024,
        backupCount=100)
    filehandler.setLevel(logging.DEBUG)
    fileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(fileformatter)
    logger.addHandler(filehandler)
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.WARNING)
    streamformatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    streamhandler.setFormatter(streamformatter)
    logger.addHandler(streamhandler)


if __name__ == '__main__':
    logdir = 'log'
    setup(logdir)
