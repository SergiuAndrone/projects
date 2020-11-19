import {t, Selector, Role} from 'testcafe';

let acceptCookies = Selector('#onetrust-accept-btn-handler');

export const cookiesAccepted = Role("https://www.hotnews.ro", async t => {
    if (await acceptCookies.exists && await acceptCookies.visible) {
        await t.click(acceptCookies);
    }
})
