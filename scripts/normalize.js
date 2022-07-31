const ethers = require('ethers')
const fs = require('fs');
const BigNumber = ethers.BigNumber
const utils = ethers.utils


try {  
    // var es_nouns = fs.readFileSync('tests/fixtures/nouns/spanish-nouns-ordered-nospaces.txt').toString().split("\n");
    // var es_verbs = fs.readFileSync('tests/fixtures/spanish-verbs-ordered-nospaces.txt').toString().split("\n");
    // var en_animals = fs.readFileSync('tests/fixtures/english-animals-ordered-nospaces.txt').toString().split("\n");
    // var es_animals = fs.readFileSync('tests/fixtures/spanish-animals-ordered-nospaces.txt').toString().split("\n");
    // var es_adjectives = fs.readFileSync('tests/fixtures/adjectives/spanish-adjectives-ordered-nospaces.txt').toString().split("\n");
    // var es_female_firstnames = fs.readFileSync('tests/fixtures/first_names/spanish-female-firstnames-ordered-nospaces.txt').toString().split("\n");
    // var es_male_firstnames = fs.readFileSync('tests/fixtures/spanish-male-firstnames-ordered-nospaces.txt').toString().split("\n");
    // var es_male_firstnames = fs.readFileSync('tests/fixtures/spanish-male-firstnames-ordered-nospaces.txt').toString().split("\n");
    var es_months_days = fs.readFileSync('tests/fixtures/spanish-months-days-ordered-nospaces.txt').toString().split("\n");

    // console.log(es_animals)
} catch(e) {
    console.log('Error:', e.stack);
}

function hash(value) {
    const labelHash = utils.keccak256(utils.toUtf8Bytes(value))
    const tokenId = BigNumber.from(labelHash).toString()
    console.log(value + "," + tokenId)
}


es_months_days.forEach(hash);