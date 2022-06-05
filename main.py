import serial

def main():
    ser = serial.Serial('COM3', baudrate=9600)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline() 
            string_data = data.decode('utf-8')
            print(string_data)

if __name__ == '__main__':
    main()