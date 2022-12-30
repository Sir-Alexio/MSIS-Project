import socket
import asyncio
import logging
import sys

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

logger = logging.getLogger(__name__)


#логгер выводит доступную информацию о девайсе
def simple_callback(device: BLEDevice, advertisement_data: AdvertisementData):
    logger.info(f"{device.address}: {advertisement_data}")
#основной метод возвращает мощность сигнала девайса/девайсов по порядку в дбМ
def getRssi(device: BLEDevice, advertisement_data : AdvertisementData):
    if device.name == "HUAWEI P smart 2019":
      print(device.name)
      print(device.rssi)
      s = socket.socket() 
     #ip сервера
      host = '192.168.100.141' 
      port = 9999
      s.connect((host, port))
      e = device.rssi
      es = str(e)
      s.send(bytes(es, encoding="UTF-8"))
      simple_callback(device, advertisement_data)
      return device.rssi


#передаю пока число, в будущем должна быть ф-я, которая обеспечивает
#связь телефона и компьютера и определяет параметры, которые будут передаваться на сервер
# e = 565
# es = str(e)
# s.send(bytes(es, encoding="UTF-8"))

#каждые 5 секунд происходит поиск девайсов
async def main(service_uuids):
    scanner = BleakScanner( getRssi, service_uuids)

    while True:
        print("(re)starting scanner")
        await scanner.start()
        await asyncio.sleep(5.0)
        await scanner.stop()
# ассинхронно запускает сканнер и записывает айдишники девайсов
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )
    service_uuids = sys.argv[1:]
    asyncio.run(main(service_uuids))