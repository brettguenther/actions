def ConfigSectionMap(creds_abs_path,section):
    import ConfigParser
    Config = ConfigParser.ConfigParser()
    Config.read(creds_abs_path)
    return dict(Config.items(section))

def initiate_logging(file_naming):
    import logging, time
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("log/" + str(time.strftime("%d_%m_%Y")) + "%s" + ".log") % (file_naming)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
