'use strict';

const { ArgumentParser } = require('argparse');
const { version } = require('../package.json');

const parser = new ArgumentParser({
    description:
        'A command line client for parsing and making folders and files for test cases using the competitive companion extension and testing the solution. Building this with an aim of making Competitive Programming More Productive'
});

parser.add_argument('-v', '--version', { action: 'version', version });
parser.add_argument('mode', {
    help: 'Allows the user to setup RCP properly',
    type: String,
    choices: ['init', 'server'],
    nargs: '?',
    default: 'server'
});

let args = parser.parse_args();
if (args.mode === 'server') {
    require('./server');
}
if (args.mode === 'init') {
    console.log('We are working on it');
}
