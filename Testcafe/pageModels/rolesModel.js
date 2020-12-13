import {t, Selector, Role} from 'testcafe';
import {profileName, profileUrl} from "./profilesModel";

let acceptCookies = Selector('#onetrust-accept-btn-handler');

export const cookiesAccepted = Role(profileUrl, async t => {
    if (await acceptCookies.exists && await acceptCookies.visible) {
        await t.click(acceptCookies);
    }
})
