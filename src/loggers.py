import logging

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
utils_file_handler = logging.FileHandler("./logs/utils.log")
utils_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)
utils_logger.addHandler(utils_file_handler)

services_logger = logging.getLogger("services")
services_logger.setLevel(logging.DEBUG)
services_file_handler = logging.FileHandler("./logs/services.log")
services_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
services_file_handler.setFormatter(services_file_formatter)
services_logger.addHandler(services_file_handler)

reports_logger = logging.getLogger("reports")
reports_logger.setLevel(logging.DEBUG)
reports_file_handler = logging.FileHandler("./logs/reports.log")
reports_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
reports_file_handler.setFormatter(reports_file_formatter)
reports_logger.addHandler(reports_file_handler)
