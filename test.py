from rainbow import RainbowLogger

if __name__ == "__main__":
  # root logger
  logger = RainbowLogger()
  logger.info("root info")
  logger.warning("root warn")
  logger.error("root error")
  logger.debug("root debug")
  logger.critical("root critical")

  logger = RainbowLogger("rainbow")
  logger.info("my info")
  logger.warning("my warn")
  logger.error("my error")
  logger.debug("my debug")
  logger.critical("my critical")

