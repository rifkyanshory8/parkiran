def simulasi_parkir_kendaraan_bermotor():
    def enqueue(parkir, x):
        parkir.append(x)
    
    def dequeue(parkir):
        if len(parkir) > 0:
            return parkir.pop(0)
        else:
            return "Parkir kosong"
    
    parkir = []

    for i in range(5):
        x = input("Masukkan kendaraan bermotor: ")
        enqueue(parkir, x)
        print("Parkir saat ini: ", parkir)
    
    print("Mulai dequeue kendaraan bermotor:")
    for i in range(5):
        print("Dequeue kendaraan bermotor: ", dequeue(parkir))
        print("Parkir saat ini: ", parkir)

simulasi_parkir_kendaraan_bermotor()
