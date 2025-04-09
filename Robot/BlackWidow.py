from SynapseWebDriver import SynapseWebDriverClass
from robot.api.deco import keyword

isFinishedGreen= False
isFinishedRed= False
isFinishedPink= False
isFinishedWhite= False
isFinishedCyan= False
isFinishedBlue= False
isFinishedOrange= False
isFinishedYellow= False

@keyword("Perform Chroma Test BlackWidow V4 Green")
def PerformChromaTestBlackWidowV4Green():
    global isFinishedGreen

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    green = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(21)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(green)

    isFinishedGreen = True

@keyword("Perform Chroma Test BlackWidow V4 Red")
def PerformChromaTestBlackWidowV4Red():
    global isFinishedRed

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    red = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(18)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(red)

    isFinishedRed = True

@keyword("Perform Chroma Test BlackWidow V4 Pink")
def PerformChromaTestBlackWidowV4Pink():
    global isFinishedPink

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    pink = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(24)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(pink)
    
    isFinishedPink= True

@keyword("Perform Chroma Test BlackWidow V4 White")
def PerformChromaTestBlackWidowV4White():
    global isFinishedWhite

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    white = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(17)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(white)
    
    isFinishedWhite= True

@keyword("Perform Chroma Test BlackWidow V4 Cyan")
def PerformChromaTestBlackWidowV4Cyan():
    global isFinishedCyan

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    cyan = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(22)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(cyan)
    
    isFinishedCyan= True

@keyword("Perform Chroma Test BlackWidow V4 Blue")
def PerformChromaTestBlackWidowV4Blue():
    global isFinishedBlue

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    blue = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(23)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(blue)
    
    isFinishedBlue= True

@keyword("Perform Chroma Test BlackWidow V4 Orange")
def PerformChromaTestBlackWidowV4Orange():
    global isFinishedOrange

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    orange = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(19)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(orange)
    
    isFinishedOrange= True

@keyword("Perform Chroma Test BlackWidow V4 Yellow")
def PerformChromaTestBlackWidowV4Yellow():
    global isFinishedYellow

    lighting_selector = '#root > div > div.nav-tabs > div.navs-wrapper > div.nav.active'
    tmp = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-dropdown > div.selected.raw-text'
    static = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.chroma-flex-row > div.dropdown-area > div.s3-options.unsetZ.flex.expand > div:nth-child(9)'
    
    colour_dropdown = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-dropdown'
    yellow = '#body-wrapper > div > div.widget-col.col-right.flex > div > div > div:nth-child(2) > div.modes-area.active > div.flex.effects-area > div > div.dropdown-area.dropdown-color > div.s3-options.flex.color-opts.expand > div:nth-child(1) > div:nth-child(20)'

    driver = SynapseWebDriverClass()
    driver.switchSynapseTabTo("BLACKWIDOW V4 75%")
    driver.clickOnElement(lighting_selector)
    driver.clickOnElement(tmp)
    driver.clickOnElement(static)

    driver.clickOnElement(colour_dropdown)
    driver.clickOnElement(yellow)
    
    isFinishedYellow= True


@keyword("Check Status Green") 
def CheckStatusGreen():
    global isFinishedGreen
    return isFinishedGreen

@keyword("Check Status Red") 
def CheckStatusRed():
    global isFinishedRed
    return isFinishedRed

@keyword("Check Status Pink") 
def CheckStatusPink():
    global isFinishedPink
    return isFinishedPink

@keyword("Check Status White") 
def CheckStatusWhite():
    global isFinishedWhite
    return isFinishedWhite

@keyword("Check Status Cyan") 
def CheckStatusCyan():
    global isFinishedCyan
    return isFinishedCyan

@keyword("Check Status Blue") 
def CheckStatusBlue():
    global isFinishedBlue
    return isFinishedBlue

@keyword("Check Status Orange") 
def CheckStatusOrange():
    global isFinishedOrange
    return isFinishedOrange

@keyword("Check Status Yellow") 
def CheckStatusYellow():
    global isFinishedYellow
    return isFinishedYellow