const fs = require('fs'); 
var namehash = require('@ensdomains/eth-ens-namehash');

var hash = namehash.hash('cártel')
console.log(hash)
// try {  
//     // var es_nouns = fs.readFileSync('tests/fixtures/es-nouns.txt').toString().split("\n");
//     var es_verbs = fs.readFileSync('tests/fixtures/es-verbs.txt').toString().split("\n");
//     console.log(es_verbs);
// } catch(e) {
//     console.log('Error:', e.stack);
// }

// // es_nouns.forEach(hash);
// es_verbs.forEach(hash);

// function hash(value) {
//     var hash = namehash.hash(value)
//     hash = hash.replace('0x', '');
//     console.log(value + "," + hash)
// }

