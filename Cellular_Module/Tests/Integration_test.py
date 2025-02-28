import time
import pytest
from Tests.UnitTest import CellularUnitTest
from utils.Logging import logger


class IntegrationTest(CellularUnitTest):
    logger.info("************************ Integration ******************************************")

    # def test_network_config(self):
    #     self.config_at.network_config()
    #     time.sleep(3)

    def test_pdp(self):
        self.config_at.pdp()
        time.sleep(3)

    def test_send_sms(self):
        self.config_at.send_sms('<ph_num>', 'Test message', 3)
        time.sleep(3)

