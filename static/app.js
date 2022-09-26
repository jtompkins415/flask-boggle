async function sendWord(){
    let word = $('#user_guess').val();

    let resp = await axios.post('/', {word});

    console.log(resp);
};

async function getWordResult(){
    let resp = await axios.get('/',)

    return resp
};



$('form').submit(function(e){
    e.preventDefault();

    sendWord();
    getWordResult();
    
});