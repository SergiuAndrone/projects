import {t, Selector} from 'testcafe';
import {cookiesAccepted} from '../pageModels/rolesModel';


fixture `test`
    .beforeEach(async t=> {
        await t.maximizeWindow();
        await t.useRole(cookiesAccepted);
        console.log('end');

})

test("first test", async t=> {
    await t.wait(5000);
    console.log('success');
})
