import smbus

class MCP4725:

    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def vol_to_num(self, vol):
        if not (0.0 <= vol <= self.dynamic_range):
            print(f"too much voltage mf ( 0.00 - {self.dynamic_range:.2f} ) B")
            print("sets 0.00 volts ...")
            return 0
        return int(vol / self.dynamic_range * 255)

    def set_number(self, number):
        if not isinstance(number,int):
            print("only int values")
        
        if not (0 <= number <= 4095):
            print("too big")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF

        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"number: {number}, data: [0x{(self.address << 1)}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, vol):
        num = self.vol_to_num(vol)
        self.set_number(num)

if __name__ == "__main__":
    
    mcp = MCP4725(5.0)
    
    try:

        while True:
            try:
                voltage = float(input("set voltage in volts: "))
                mcp.set_voltage(voltage)

            except ValueError:
                print("Not a number, try again mf")

    finally:
        mcp.deinit()