import socket

def calc_kg(kg):
        if kg < 1:
                pri = 6.0
        elif kg >= 1 and kg < 2:
                pri = 7.0
        elif kg >= 2 and kg < 3:
                pri = 8.0
        elif kg >= 3 and kg < 4:
                pri = 9.0
        elif kg >= 4 and kg < 5:
                pri = 10.0
        elif kg >= 5 and kg < 6:
                pri = 12.0
        else:
                return 0

        return pri;

def calc_area(area,pri):

        sou = ["N9","JHR","MLK"]
        nor = ["PLS","KDH","PNG","PRK"]
        eas = ["KLN","PHG","TRG"]
        cent = ["SEL","LBN","KUL","PYJ"]

        if area in cent:
            tot = pri + 8.0
        elif area in sou:
            tot = pri + 12.0
        elif area in nor:
            tot = pri + 13.0
        elif area in eas:
            tot = pri + 14.0
        elif area == "SWK":
            tot = pri + 15.0
        elif area == "SBH":
            tot = pri + 15.0
        else:
            print("Area code not valid.")

        return tot;

def details():
    print("\n\n-Sender information-");
    sender_name = input("\nSender name : ");
    sender_phone = int(input("Sender phone : "));
    sender_add = input("Sender address : ");

    print("\n\n-Receiver information-");
    receiver_name = input("\nReceiver name : ");
    receiver_phone = int(input("Receiver phone : "));
    receiver_add = input("Receiver address: ");
    return sender_name,sender_add,sender_phone,receiver_name,receiver_add,receiver_phone;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '192.168.54.4'
port = 8888

print('Waiting for connection')
try:
    s.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    counter = input("IP Address : ")
    s.send(str.encode(counter))

    file = open('parcel.txt','a')

    detail = details();
    kg = float(input("\nEnter parcel weight (kg) : ")) ;
    price = calc_kg(kg);
    #s.send(pri)

    print("\nSEL - SELANGOR\nPYJ - PUTRAJAYA\nLBN - LABUAN\nKUL - KUALA LUMPUR");
    print("N9 - NEGERI SEMBILAN\nMLK - MELAKA\nJHR - JOHOR");
    print("KDH - KEDAH\nPRK - PERAK\nPNG - PULAU PINANG\nPLS - PERLIS");
    print("KLN - KELANTAN\nPHG - PAHANG\nTRG - TERENGGANU\nSBH - SABAH\nSWK - SARAWAK");

    area = input("\nEnter code area : ");
    total = calc_area(area,price);
    print("The total price is : RM " + str(total))
    #s.send(str.encode(total))

    count = 000;
    if count >= 0:
        x = 100;
    x = x + 3;
    combine_code = area + "MAS";
    tracking_num = combine_code + str(x);
    x = x + 3;
    print("Tracking Number : " + tracking_num);

    break


file.write(f'{detail,area,tracking_num,total}\n')

file.close()

file = open('parcel.txt','r')
r = file.read()
s.send(str.encode(r))

s.close()
