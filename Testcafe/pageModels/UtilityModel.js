import {driver, windowsAppDriverCapabilities, By2} from 'selenium-appium';

const appId = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App';


class UtilityModel {
    constructor() {
        this.oneButton = By2.nativeName('One');
        this.plusButton = By2.nativeName('Plus');
        this.sevenButton = By2.nativeName('Seven');
        this.equalButton = By2.nativeName('Equals');
        this.calculatorResult = By2.nativeAccessibilityId('CalculatorResults');
    }

    async setup() {
        const capabilities = windowsAppDriverCapabilities(appId);
        return driver.startWithCapabilities(capabilities);
    }

    async teardown() {
        return driver.quit();
    }

}

export default new UtilityModel();

