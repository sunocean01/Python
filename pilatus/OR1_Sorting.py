import sys, os, shutil
import time
import numpy as np
import logging

from pilatus.target import Target
from pilatus import conversion
from pilatus.fwdownload_native import TargetLauncher
import datetime
date_raw = datetime.datetime.now()

import L1Colibri as Colibri
import L1Colibri.L2Dsb as Dsb
import L1Colibri.L2Dsb.L3Afb as Afb
import L1Colibri.L2Dsb.L3Afb.L4ApplicationSetup as App
import L1Colibri.L2Dsb.L3Afb.L4ApplicationSetup.L5CommonModule as Module
import L1Colibri.L2Dsb.L3Afb.L4ApplicationSetup.L5CommonModule.L6Mono as Mono

# ###################################################################################

logger = logging.getLogger('Parrot - Flashing')
logger.setLevel(logging.DEBUG)
date_processed = "{}{}{}-{}_{}_{}".format(date_raw.year, date_raw.month,
                  date_raw.day, date_raw.hour, date_raw.minute, date_raw.second)
fh = logging.FileHandler('{}-Parrot_Flashing.log'.format(date_processed))
ch = logging.StreamHandler()

ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


fh.setLevel(logging.INFO)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


PILATUS_IP_0 = "192.168.100.100"
CHIP_REV = ('B', 0)
# ###################################################################################

logger.info('Start process...')
logger.info('Initialize Pilatus 0.')

# run & initialise firmware
target_0 = Target()
target_0.connect(PILATUS_IP_0)
target_0.build_and_init(CHIP_REV, layer=6, access_level=Colibri.ietIceAccessLevel.eIceAccLevelExpert)

hw_l4_0 = target_0.hw_identification_reader.GetConnectedHw(4)
assert hw_l4_0.HwType == 'PilatusMultiModuleTester', 'you must connect a MMT'

mmt_0 = App.WrapMultiModuleTesterPrx.checkedCast(target_0.L4Factory.CreateProxy("MultiModuleTester"))
hw_per_0 = mmt_0.GetModuleTesterPeripheryHw()
#assert not hw_per_0.HwType == 'PmCalibration', 'you must connect / fake PmCalibration HW'



pm_0 = App.WrapPmCalibrationPrx.checkedCast(target_0.L4Factory.CreateProxy("PmCalibration"))
# get some fw objects
broker_0 = Mono.WrapL6FactoryPrx.checkedCast(target_0.session.GetFactory(6)).GetBroker()
pwr_0 = broker_0.GetMonoPower()
calibif_0 = broker_0.GetFairfieldCalibInterface()



PILATUS_IP_1 = "192.168.100.101"

# ###################################################################################


logger.info('Initialize Pilatus 1.')

# run & initialise firmware
target_1 = Target()
target_1.connect(PILATUS_IP_1)
target_1.build_and_init(CHIP_REV, layer=6, access_level=Colibri.ietIceAccessLevel.eIceAccLevelExpert)

hw_l4_1 = target_1.hw_identification_reader.GetConnectedHw(4)
assert hw_l4_1.HwType == 'PilatusMultiModuleTester', 'you must connect a MMT'

mmt_1 = App.WrapMultiModuleTesterPrx.checkedCast(target_1.L4Factory.CreateProxy("MultiModuleTester"))
hw_per_1 = mmt_1.GetModuleTesterPeripheryHw()
#assert not hw_per_1.HwType == 'PmCalibration', 'you must connect / fake PmCalibration HW'



pm_1 = App.WrapPmCalibrationPrx.checkedCast(target_1.L4Factory.CreateProxy("PmCalibration"))
# get some fw objects
broker_1 = Mono.WrapL6FactoryPrx.checkedCast(target_1.session.GetFactory(6)).GetBroker()
pwr_1 = broker_1.GetMonoPower()
calibif_1 = broker_1.GetFairfieldCalibInterface()


mmt_0.WriteDutLeds([False] * 32)
mmt_1.WriteDutLeds([False] * 32)

time.sleep(2)

# lock tray (sorting station only)
time.sleep(1)
mmt_0.Set24VOutput(1)
time.sleep(1.3)
mmt_0.Set24VOutput(2)
time.sleep(1.5)

while True:

    # apply power & com masks
    target_0.dsb.dut_channel_ctrl.SetPowerMask([True] * 32)
    target_0.dsb.dut_channel_ctrl.SetComMask([True] * 32)
    target_1.dsb.dut_channel_ctrl.SetPowerMask([True] * 32)
    target_1.dsb.dut_channel_ctrl.SetComMask([True] * 32)
    
    input("继续请按Enter键（Press <enter> to continue）")


    pwr_0.PowerOn()
    pwr_1.PowerOn()

    err_0, serials_connected_0 = calibif_0.ReadSerialNumber()
    err_1, serials_connected_1 = calibif_1.ReadSerialNumber()


    firmware_0 = broker_0.GetMonoFirmwareDownload()
    firmware_1 = broker_1.GetMonoFirmwareDownload()

    logger.info("Flash sensors...")

    with open("Parrot_v1.0.hex") as f:
        firmware_0.DownloadHexFile(f.read())
        
    with open("Parrot_v1.0.hex") as f:
        firmware_1.DownloadHexFile(f.read())
        
    led_0 = [False if (calibif_0.ReadDeviceVersion()[1][ch].FwMajor == 1) and (calibif_0.ReadDeviceVersion()[1][ch].FwMinor == 0) else True for ch, serial in enumerate(serials_connected_0)]
    led_1 = [False if (calibif_1.ReadDeviceVersion()[1][ch].FwMajor == 1) and (calibif_1.ReadDeviceVersion()[1][ch].FwMinor == 0) else True for ch, serial in enumerate(serials_connected_1)]

    mmt_0.WriteDutLeds(led_0)
    mmt_1.WriteDutLeds(led_1)


    serials_whitelist_0 = [serial for ch, serial in enumerate(serials_connected_0) if (calibif_0.ReadDeviceVersion()[1][ch].FwMajor == 1) and (calibif_0.ReadDeviceVersion()[1][ch].FwMinor == 0)]
    serials_blacklist_0 = [serial for serial in serials_connected_0 if serial not in serials_whitelist_0 and serial is not ""]
    serials_whitelist_1 = [serial for ch, serial in enumerate(serials_connected_1) if (calibif_1.ReadDeviceVersion()[1][ch].FwMajor == 1) and (calibif_1.ReadDeviceVersion()[1][ch].FwMinor == 0)]
    serials_blacklist_1 = [serial for serial in serials_connected_1 if serial not in serials_whitelist_1 and serial is not ""]

    with open("serials_whitelist.txt", "a") as f:
        [f.write(s + "\n") for s in serials_whitelist_0]

    with open("serials_blacklist.txt", "a") as f:
        [f.write(s + "\n") for s in serials_blacklist_0]

    with open("serials_whitelist.txt", "a") as f:
        [f.write(s + "\n") for s in serials_whitelist_1]

    with open("serials_blacklist.txt", "a") as f:
        [f.write(s + "\n") for s in serials_blacklist_1]

    input('所有不良品已移除；确认请按Enter键（Sort out all sensors that were not flashed correctly. Then press <enter>.）')

    pwr_0.PowerOff()
    pwr_1.PowerOff()

    logger.info("Flashed DUTs: {}".format([serial for serial in serials_whitelist_0 + serials_whitelist_1]))
    logger.info("Blacklisted DUTs (DUTs that were not flashed correctly): {}".format([serial for serial in serials_blacklist_0 + serials_blacklist_1]))
    logger.info("Flashing of sensors is done.")

    mmt_0.WriteDutLeds([False] * 32)
    mmt_1.WriteDutLeds([False] * 32)
    
    print("刷写完成，确认所有已刷产品已移除，未刷产品已装满托盘，请按回车继续刷写，按任意键+Enter退出程序（Press enter to start a new round. Press any key&enter to exit）")
    str = input()
    if str == "":
        pass
    else:
        break

# unlock tray (sorting station only)
mmt_0.Clear24VOutput(2)
time.sleep(0.3)
mmt_0.Clear24VOutput(1)
logger.info("请移除所有产品(Remove all flashed sensors from tray.)")

