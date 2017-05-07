$(document).ready(function(){
    console.log('ready info.');
    $('a').on('click', function(event){
        console.log('You\'r click a link');
        event.preventDefault();
        return false;
    })
});
