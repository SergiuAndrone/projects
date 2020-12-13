import UtilityModel from "../pageModels/UtilityModel.js";

// fixture('suite 1', async t => {
//
// })
//
// test('test 1', async t => {
//
//     await UtilityModel.setup();
//
//     await UtilityModel.oneButton.click();
//     await UtilityModel.plusButton.click();
//     await UtilityModel.sevenButton.click();
//     await UtilityModel.equalButton.click();
//
//     let result = await UtilityModel.calculatorResult.getText();
//
//     console.log(result);
//
//     await UtilityModel.teardown();
// })


async function runTest() {
    await UtilityModel.setup();

    await UtilityModel.oneButton.click();
    await UtilityModel.plusButton.click();
    await UtilityModel.sevenButton.click();
    await UtilityModel.equalButton.click();

    let result = await UtilityModel.calculatorResult.getText();

    console.log(result);

    await UtilityModel.teardown();
}
await runTest()