let wordGuess = $('form').val();

$('form').submit(function(e){
    e.preventDefault();
});

async function sendWord() {
    const resp = await axios.post('/',data);

    console.log(resp);
}