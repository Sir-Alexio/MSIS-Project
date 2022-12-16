import asyncio
import logging
import sys

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData


# для работы требуются библиотеки pybluez, asyncio, bleak
# определяет девайсы с low energy bluetooth
# для определения телефона нужно запустить nRF Connect на телефоне
# и создать новый сервис который будет раздавать сигнал по нужной технологии
logger = logging.getLogger(__name__)

#логгер выводит доступную информацию о девайсе
def simple_callback(device: BLEDevice, advertisement_data: AdvertisementData):
    logger.info(f"{device.address}: {advertisement_data}")
#основной метод возвращает мощность сигнала девайса/девайсов по порядку в дбМ
def getRssi(device: BLEDevice, advertisement_data : AdvertisementData):
    print(device.name)
    print(device.rssi)
    simple_callback(device, advertisement_data)
    return device.rssi


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