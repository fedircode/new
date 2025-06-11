import logging as log

log.basicConfig(level=log.WARNING,
format="%(asctime)s: %(levelname)s: [%(filename)s]:%(lineno)s %(message)s",
datefmt="%I:%M:%S %p",
handlers=[
    # log.FileHandler("capa_datos.log"),
    log.FileHandler("logger.log"),
    log.StreamHandler()
])



if __name__ == "__main__":
    log.debug("mensaje a nivel debug")
    log.info("mensaje a nivel de info")
    log.warning("mensaje a nivel de warning")
    log.error("mensaje a nivel de error")
    log.critical("mensaje a nivel de critical")