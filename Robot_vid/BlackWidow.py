from SynapseWebDriver import SynapseWebDriverClass
from robot.api.deco import keyword
import asyncio

isFinishedSpectrum= False
isFinishedStarlight= False
isFinishedWave= False

lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div:nth-child(2)'
pattern_dropdown = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown'
static = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9) > div'
# colour_dropdown = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
spectrum = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(7) > div'
starlight = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(8) > div'
wave = '#body-wrapper > div > div.widget-col.col-right > div > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(10) > div'

# async def delay3():
#     print("Waiting 3 seconds...")
#     await asyncio.sleep(3)
#     print("Done!")

async def delay():
    print("Waiting 1 seconds...")
    await asyncio.sleep(0.5)
    print("Done!")

@keyword("Perform Chroma Test BlackWidow V4 Spectrum")
def PerformChromaTestBlackWidowV4Spectrum():
    global isFinishedSpectrum

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    asyncio.run(delay())
    driver.clickOnElement(pattern_dropdown)
    asyncio.run(delay())
    driver.clickOnElement(spectrum)
    asyncio.run(delay())

    isFinishedSpectrum = True
    # asyncio.run(delay3())

@keyword("Perform Chroma Test BlackWidow V4 Starlight")
def PerformChromaTestBlackWidowV4Starlight():
    global isFinishedStarlight

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    asyncio.run(delay())
    driver.clickOnElement(pattern_dropdown)
    asyncio.run(delay())
    driver.clickOnElement(starlight)
    asyncio.run(delay())

    isFinishedStarlight = True
    # asyncio.run(delay3())

@keyword("Perform Chroma Test BlackWidow V4 Wave")
def PerformChromaTestBlackWidowV4Wave():
    global isFinishedWave

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    asyncio.run(delay())
    driver.clickOnElement(pattern_dropdown)
    asyncio.run(delay())
    driver.clickOnElement(wave)
    asyncio.run(delay())

    isFinishedWave = True
    # asyncio.run(delay3())

@keyword("Check Status Spectrum") 
def CheckStatusSpectrum():
    global isFinishedSpectrum
    return isFinishedSpectrum

@keyword("Check Status Wave") 
def CheckStatusWave():
    global isFinishedWave
    return isFinishedWave

@keyword("Check Status Starlight") 
def CheckStatusStarlight():
    global isFinishedStarlight
    return isFinishedStarlight