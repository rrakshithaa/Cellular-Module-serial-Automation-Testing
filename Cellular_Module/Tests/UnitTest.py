import logging
import re
import time
import unittest
from utils.Logging import logger
from Device.config import ConfigATCommands


class CellularUnitTest(unittest.TestCase):
    logger.info("************************************** Unit Test ***********************************")


    @classmethod
    def setUpClass(cls):
        cls.config_at = ConfigATCommands()


    @classmethod
    def tearDownClass(cls):
        cls.config_at.close()

    def test_network_registration_status(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        print(response)
        time.sleep(5)
        assert response == "AT command\r\r\nAT command (0-2)\r\n\r\nOK\r\n"
        logger.info(f"Command: {command}\nResponse: {response}")
        time.sleep(3)

    def test_signal_quality(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        pattern = r"AT command\r\r\n\+AT command \d{1,2},\d{1,2}\r\n\r\nOK\r\n"
        assert re.match(pattern, response)
        logger.info(f"Command: {command.strip()}\nResponse: {response.strip()}")
        time.sleep(3)

    def test_manufacturer_identification(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        assert response == "AT command\r\r\nTelit\r\n\r\nOK\r\n"
        logger.info(f"Command: {command}\nResponse: {response}")
        time.sleep(3)

    def test_model_identification(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        assert response == "AT command\r\r\nModel num\r\n\r\nOK\r\n"
        logger.info(f"Command: {command}\nResponse: {response}")
        time.sleep(3)

    def test_revision_identification(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        time.sleep(3)
        assert response == "AT command\r\r\nM0C number\r\n\r\nOK\r\n"
        logger.info(f"Command: {command}\nResponse: {response}")
        time.sleep(3)

    def test_serial_num_identification(self):
        command = "AT command"
        self.config_at.ser.write((command + '\r').encode())
        response = self.config_at.read_response()
        assert response == "AT command\r\r\nserial number\r\n\r\nOK\r\n"
        logger.info(f"Command: {command}\nResponse: {response}")
        time.sleep(3)


# if __name__ == '__main__':
#     unittest.main()

