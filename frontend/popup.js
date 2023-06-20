document.getElementById('sendrequest').addEventListener('click', function() {
    var apiUrl = 'http://127.0.0.1:8000/api/get_openai_summary/?topic=Hello';  // Replace with your API endpoint URL

        fetch(apiUrl)
        .then(function(response) {
            if (!response.ok) {
            throw new Error('Error: ' + response.status);
            }
            return response.json();
        })
        .then(function(data) {
            var resultElement = document.getElementById('result');
            resultElement.textContent = data.data;  
            console.log(data);  
        })
        .catch(function(error) {
            console.log('Request failed:', error);
        });

});