const args = require('minimist')(process.argv.slice(2));

const profiles = {dev: 'https://www.hotnews.ro',
                  stg: 'https://www.youtube.com'};

export const profileUrl = profiles[args.profile];
export const profileName = args.profile;

