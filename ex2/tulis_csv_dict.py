import csv

with open('contacts.csv', mode='a') as csv_file:
    # menentukan label
    fieldnames = ['NO', 'NAMA', 'TELEPON']
    
    # membuat objek writer
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # menulis baris ke file CSV
    writer.writeheader()
    writer.writerow({'NO': '10', 'NAMA': 'Via Vallen', 'TELEPON': '02109999'})
    writer.writerow({'NO': '11', 'NAMA': 'M. Andi', 'TELEPON': '02148488888'})
    
print("Writing Done!")
