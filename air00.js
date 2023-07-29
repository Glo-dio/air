// fonctions utilisées

function ma_fonction(str, string_séparateur)
{
	let word = [];
	let tableau = [];
	let tmp = []
	let i = 0;
	
	while (str.charCodeAt(i) == 32 || str.charCodeAt(i) == 9 || str.charCodeAt(i) == 10)
		i++;
	
	while(i <= str.length)
	{
		
		if (((str.charCodeAt(i) == 32 || str.charCodeAt(i) == 9 || str.charCodeAt(i) == 10) 
			&& (str.charCodeAt(i + 1) > 64 && str.charCodeAt(i + 1) < 91
			|| str.charCodeAt(i + 1) > 96 && str.charCodeAt(i + 1) < 123)
			|| i == str.length))
		{
			tmp.push(String(word.join('')));
			tableau.push(tmp);
			tmp = [];
			word = [];
		}
		else
			word.push(str[i]);
		i++;
	}
	return (tableau)
}

function is_arg_valid()
{
	if (is_nb_arg_correct === false)
		return false;
}

// Partie 1 : Gestion d'erreur
is_nb_arg_correct = process.argv.length === 3;

if (is_arg_valid() === false)
{
	console.log("error");
	process.exit(1);
}	
	
// Partie 2 : Parsing
const arg = process.argv[2];

// Partie 3 : Résolution
const answer = ma_fonction(arg,'g');

// Partie 4 : Affichage
for (let i in answer)
	console.log(String(answer[i]))

