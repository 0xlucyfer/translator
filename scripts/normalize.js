const ethers = require('ethers')
const fs = require('fs');
const BigNumber = ethers.BigNumber
const utils = ethers.utils


try {  
    var data = fs.readFileSync('tests/fixtures/spanish-months-days-normalized.txt').toString().split("\n");
    // console.log(es_animals)
} catch(e) {
    console.log('Error:', e.stack);
}

function hash(value) {
    const labelHash = utils.keccak256(utils.toUtf8Bytes(value))
    const tokenId = BigNumber.from(labelHash).toString()
    console.log(value + "," + tokenId)
}


data.forEach(hash);