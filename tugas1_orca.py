class KomponenROV:
    def __init__(self, nama: str, status: str):
        self.nama = nama
        self.status = status

    def info(self):
        print(f"Nama: {self.nama}, Status: {self.status}.")

class Thruster(KomponenROV):
    def __init__(self, nama: str, status: str, power: float):
        KomponenROV.__init__(self, nama, status)
        self.power = power

    def info(self):
        print(f"Thruster | Nama: {self.nama}, Status: {self.status}, Power: {self.power}")

class Sensor(KomponenROV):
    def __init__(self, nama: str, status: str, nilai: float):
        KomponenROV.__init__(self, nama, status)
        self.nilai = nilai

    def info(self):
        print(f"Sensor | Nama: {self.nama}, Status: {self.status}, Nilai Sensor: {self.nilai}")

def main():
    num_components = int(input().strip())
    components = []

    for _ in range(num_components):
        line = input().strip().split()
        jenis, nama, status, nilai_raw = line[0], line[1], line[2], line[3]

        if jenis == "Thruster":
            power = float(nilai_raw)
            components.append(Thruster(nama, status, power))
        elif jenis == "Sensor":
            nilai = float(nilai_raw)
            components.append(Sensor(nama, status, nilai))

    print(f"\nJumlah komponen: {len(components)}")
    for comp in components:
        comp.info()

if __name__ == "__main__":
    main()