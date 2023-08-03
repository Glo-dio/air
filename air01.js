// fonctions utilisées

function custom_include(array, element)
{
	for (let i = 0; i < array.length; i++)
	{
		if (array[i] === element)
			return true;
	}
	return false;
}

function ma_fonction(str, string_séparateur)
{
	let word = [];
	let tableau = [];
	let tmp = []
	let i = 0;
	let j = 0;
	let k = 0;

	
	while(i <= str.length)
	{
		// if (str.charAt(i) !== string_séparateur.charAt(1) || str.charAt(i - 1) !== string_séparateur.charAt(0))
		if (str.charAt(i) !== string_séparateur.charAt(0) || str.charAt(i + 1) !== string_séparateur.charAt(1))
		{
			if (i == str.length)
			{
				tmp.push(String(word.join('')));
				tableau.push(tmp);
			}
			// console.log("Youpi")
			word.push(str[i]);
		}
		else
		{

			for (j = 0; j < string_séparateur.length; j++)
			{
				// if (str[i + j] != string_séparateur[j])
				if (str.charAt(i + j) !== string_séparateur.charAt(j))
				{
					k = i + j - 1
					// for (; j > 0; j--)
					// for (let k = 0; k < j; k++)
					// while(i < k)
					// {
						word.push(str[i]);
						console.log(`down ${k}`);
					// 	// i++;
						// i++;
					// }
					// i += 2;
					break;
				}
				// else
				// {
				// 	console.log(`${j}`);
				// }
			}
			tmp.push(String(word.join('')));
			tableau.push(tmp);
			tmp = [];
			word = [];
			i += string_séparateur.length - 1
		}
		i++;
	}
	return (tableau)
}

function is_arg_valid()
{
	if (is_nb_arg_correct === false)
		return false;

	if (process.argv[3].length < 2)
		return false;
}

// Partie 1 : Gestion d'erreur
is_nb_arg_correct = process.argv.length === 4;

if (is_arg_valid() === false)
{
	console.log("error");
	process.exit(1);
}

// Partie 2 : Parsing
const arg = process.argv[2];
const separator = process.argv[3];
console.log(`max i = ${arg.length - 1}`)

// Partie 3 : Résolution
const answer = ma_fonction(arg, separator);

// Partie 4 : Affichage
for (let i in answer)
	console.log(answer[i])


