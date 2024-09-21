import psutil

def cpu_usage():
    print(f"Uso da CPU: {psutil.cpu_percent(interval=1)}%")

def memory_usage():
    memory = psutil.virtual_memory()
    print(f"Uso de Memória: {memory.percent}% (Usado: {memory.used / (1024 ** 2):.2f} MB, Livre: {memory.available / (1024 ** 2):.2f} MB)")

def disk_usage():
    disk = psutil.disk_usage('/')
    print(f"Uso de Disco: {disk.percent}% (Usado: {disk.used / (1024 ** 3):.2f} GB, Livre: {disk.free / (1024 ** 3):.2f} GB)")

def main():
    print("Monitor de Sistema")
    cpu_usage()
    memory_usage()
    disk_usage()

if __name__ == "__main__":
    main()
