const fs = require('fs'); 
var namehash = require('@ensdomains/eth-ens-namehash');


try {  
    var es_nouns = fs.readFileSync('tests/fixtures/spanish-nouns.txt').toString().split("\n");
    var es_verbs = fs.readFileSync('tests/fixtures/spanish-verbs.txt').toString().split("\n");
    var en_animals = fs.readFileSync('tests/fixtures/english-animals-nospaces.txt').toString().split("\n");
    var es_animals = fs.readFileSync('tests/fixtures/spanish-animals-nospaces.txt').toString().split("\n");
    // console.log(es_animals)
} catch(e) {
    console.log('Error:', e.stack);
}

// es_nouns.forEach(hash);
// console.log('\n\n\n\n');
// es_verbs.forEach(hash);
// console.log('\n\n\n\n');
// en_animals.forEach(hash);
// console.log('\n\n\n\n');
es_animals.forEach(hash)


function hash(value) {
    var hash = namehash.hash(value)
    hash = hash.replace('0x', '');
    console.log(value + "," + hash)
}

