const ethers = require('ethers')
const fs = require('fs');
const BigNumber = ethers.BigNumber
const utils = ethers.utils


try {  
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