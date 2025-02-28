import re
import time
import serial
from click import command

from utils.Logging import logger


class ConfigATCommands:
    def __init__(self, port="<port>", baudrate=115200, timeout=10):
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def read_response(self):
        response = ""
        start_time = time.time()
        while True:
            if self.ser.in_waiting > 0:
                response += self.ser.read(self.ser.in_waiting).decode("utf-8", errors='replace')
                print(f"Intermediate response: {response}")  # Debugging line
                if "OK" in response:
                    break
            if time.time() - start_time > 10:  # Timeout after 10 seconds
                print("Timeout reached")
                break
            time.sleep(0.1)  # Add a small delay to avoid busy-waiting
        return response

    def close(self):
        self.ser.close()


    def pdp(self):
        command = "<pdp_AT_command>"    # AT command which is vulnerable to Telit modules
        self.ser.write((command + '\r').encode())
        response = self.read_response()
        time.sleep(5)
        pattern = r'1,"IP","internet","",0,0,0,0'
        match = re.search(pattern, response)

        if match.group() in response:
            command1 = f"<pdp_AT_command={match.group()}"
            self.ser.write((command1 + '\r').encode())
            response1 = self.read_response()
            logger.info(f"Second pdp Command: {command1}\nResponse: {response1}")
        else:
            logger.error("Couldn't Find the pattern!!!")


    def send_sms(self,phone_num, message, count):
        for i in range(count):
            self.ser.write(b'sms_AT_command\r')     # AT command which is vulnerable to Telit modules
            time.sleep(2)
            self.ser.write(b'sms_AT_command'+phone_num.encode() + b'",145\r')       # AT command which is vulnerable to Telit modules
            time.sleep(2)
            self.ser.write(message.encode() + b'\x1A')  # Send message and Ctrl+Z
            time.sleep(3)
            response = self.read_response()
            logger.info(f"SMS Command: {command}\nResponse: {response}")

    def network_config(self):
        subscriber_num = b'subscriber num _AT_command\r'        # AT command which is vulnerable to Telit modules
        self.ser.write(subscriber_num)
        sub_response = self.read_response()
        logger.info(f"Subscriber Command:{subscriber_num} \n Subscriber Response:{sub_response}")
        time.sleep(3)
        print()
        operator_selection = b'opeartor selection_AT_command\r'     # AT command which is vulnerable to Telit modules
        self.ser.write(operator_selection)
        operator_response = self.read_response()
        logger.info(f"Operator Selection Command:{operator_selection} \n Subscriber Response:{operator_response}")
        time.sleep(3)
        print()
