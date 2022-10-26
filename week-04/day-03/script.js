const generateBtn = document.body.querySelector("#generate-btn");
generateBtn.addEventListener("click", async () => {
    const images = document.body.querySelectorAll("img");
    for (let image of images)
        image.remove();

    let response = await axios.get("https://pokeapi.co/api/v2/pokemon");

    let count = response.data.count;
    response = await axios.get(`https://pokeapi.co/api/v2/pokemon?limit=${count}`);

    let randomIdx = Math.floor(Math.random() * count);
    let randomPokemon = [];
    randomPokemon.push(await axios.get(`${response.data.results[randomIdx].url}`));

    for (let i = 0; i < 5; i++) {
        randomIdx = Math.floor(Math.random() * randomPokemon[0].data.types.length);
        let type = await axios.get(`${randomPokemon[0].data.types[randomIdx].type.url}`);
        randomIdx = Math.floor(Math.random() * type.data.pokemon.length);

        randomPokemon.push(await axios.get(`${type.data.pokemon[randomIdx].pokemon.url}`));
    }

    for (let pokemon of randomPokemon) {
        const image = new Image();
        image.src = pokemon.data.sprites.front_default;
        document.body.appendChild(image);
    }
});