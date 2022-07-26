var namehash = require('@ensdomains/eth-ens-namehash')
// var hash = namehash.hash('foo.eth')


const test = ['abada',
'abeja',
'alacrán',
'alce',
'almeja',
'alpáca',
'anchoa',
'anguila',
'antílope',
'araña',
'atún',
'atún',
'avestruz',
'avispa',
'avispón',
'avispón',
'bacalao',
'bagre',
'ballena',
'ballenaasesina',
'ballenaazul',
'ballenabarbada',
'ballenajorobada',
'bisonte',
'boaconstrictora',
'bongo',
'bonobo',
'buey',
'bufalo',
'buitre',
'buitre',
'burro',
'búfala',
'búfalo',
'búho',
'caballito',
'caballitodemar',
'caballo',
'cabra',
'cacatúa',
'caimán',
'calamar',
'calamar',
'camaleón',
'camaleón',
'camarón',
'camarón',
'camella',
'camello',
'camello',
'canaria',
'cangrejo',
'cangrejo',
'canguro',
'canguro',
'carnero',
'cebra',
'cerdo',
'chango',
'changos',
'chimpancé',
'chimpancé',
'chimpancés',
'chita',
'ciervo',
'cisne',
'cobra',
'cocodrilo',
'colibrí',
'comadreja',
'conejo',
'correcaminos',
'coyote',
'crustáceo',
'culebra',
'cóndor',
'delfín',
'delfín',
'dragón',
'dragóndekomodo',
'dragónkomodo',
'elefante',
'elefante',
'emú',
'escarabajo',
'escorpión',
'estornino',
'estrellademar',
'faisán',
'falcón',
'foca',
'foca',
'fringílido',
'gacela',
'gallina',
'gallo',
'gamba',
'gamba',
'golondrina',
'gorila',
'gorila',
'gorrión',
'grantiburónblanco',
'grillo',
'grulla',
'guepardo',
'hiena',
'hiena',
'hipopótama',
'hipopótamo',
'hormiga',
'iguana',
'impala',
'jabalí',
'jabalí',
'jabalí',
'jabalíverrugoso',
'jaguaresa',
'jirafa',
'jirafa',
'lagartija',
'lagarto',
'langosta',
'lechuza',
'leopardo',
'leopardo',
'leopardodenieve',
'león',
'leónmarino',
'libélula',
'libélula',
'liebre',
'loba',
'lobina',
'lobo',
'lobo',
'macaco',
'manatí',
'mangosta',
'manturón',
'mapache',
'mejillón',
'milpiés',
'mirlo',
'mirlo',
'mofeta',
'mono',
'monoaraña',
'mosca',
'narval',
'ocelote',
'orangután',
'ornitorrinco',
'ornitorrinco',
'osa',
'osezno',
'oso',
'osohimalayo',
'osohormiguero',
'osopanda',
'osopanda',
'ostión',
'oveja',
'paloma',
'palomo',
'pandarojo',
'pangolín',
'pantera',
'pantera',
'pantera',
'papio',
'pavo',
'pelícano',
'perezosa',
'perezosa',
'perezoso',
'perezoso',
'pez',
'pezespada',
'pezpayaso',
'pichón',
'pingüino',
'pingüino',
'pingüino',
'pintada',
'pinzón',
'piraña',
'piraña',
'pitón',
'pollo',
'pulga',
'pulpo',
'puma',
'pájaro',
'pájaro',
'rana',
'ratón',
'rinoceronte',
'rinoceronte',
'rinoceronte',
'salmón',
'salmón',
'salmón',
'sapa',
'sapo',
'serpiente',
'serpiente',
'serpiente',
'serpientedecascabel',
'serpientemarina',
'tarántula',
'tejón',
'tejónbitcoin',
'tejónbtc',
'termita',
'tiburónblanco',
'tiburónmartillo',
'tiburóntigre',
'tigre',
'tigreblancosiberiano',
'tigredeamur',
'tigredebali',
'tigredechina',
'tigredesumatra',
'tigreindio',
'tigreindochino',
'tigremalayo',
'tigresa',
'tigresiberiano',
'tigresumatra',
'tortuga',
'tortugamarina',
'trucha',
'tucán',
'venado',
'visón',
'viudanegra',
'víbora',
'zarigueya',
'zarigüeya',
'zorra',
'zorrillo',
'zorrillo',
'zorro']

test.forEach(hash);

function hash(value) {
    var hash = namehash.hash(value)
    hash = hash.replace('0x', '');
    console.log(value + "," + hash)
}

