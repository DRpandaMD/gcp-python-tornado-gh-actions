document.addEventListener('DOMContentLoaded', function() {    
    (function() {
        var header = document.getElementsByTagName('h1')[0];
        var message = document.getElementsByTagName('p')[0];
        var button = document.getElementsByTagName('button')[0];
    
        button.addEventListener('click', function() {
        header.style.color = getRandomColor();
        message.style.fontSize = getRandomFontSize() + 'em';
        });
    
        function getRandomColor() {
        var letters = '0123456789ABCDEF';
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
        }
    
        function getRandomFontSize() {
        return Math.floor(Math.random() * 5) + 1;
        }
    })();
});
