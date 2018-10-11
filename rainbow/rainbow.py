"""
:Author: Almer Mendoza
:Since: 10/10/2018
"""
import logging

def RainbowLogger(name=None, no_time=False):
  """
  A customized logger built on top of Python's logging
  """
  MAGENTA = '\033[95m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  GREY = '\033[0m'
  WHITE = '\033[1m'

  logging.addLevelName(logging.DEBUG, '{}{}\t{}'.format(WHITE, logging.getLevelName(logging.DEBUG), GREY))
  logging.addLevelName(logging.INFO, '{}{}\t{}'.format(GREEN, logging.getLevelName(logging.INFO), GREY))
  logging.addLevelName(logging.WARNING, '{}{}\t{}'.format(YELLOW, logging.getLevelName(logging.WARNING), GREY))
  logging.addLevelName(logging.ERROR, '{}{}\t{}'.format(RED, logging.getLevelName(logging.ERROR), GREY))
  logging.addLevelName(logging.CRITICAL, '{}{}\t{}'.format(MAGENTA, logging.getLevelName(logging.CRITICAL), GREY))

  logger = logging.getLogger(__name__ if name is None else name)
  handler = logging.StreamHandler()
  formatter = logging.Formatter('{}%(asctime)s %(name)-12s %(levelname)-8s %(message)s{}'.format(BLUE, GREY))
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.DEBUG)

  return logger
