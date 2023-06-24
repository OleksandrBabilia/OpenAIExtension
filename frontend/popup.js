document.getElementById('send-request').addEventListener('click', function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var activeTab = tabs[0];
        var apiUrl = 'http://127.0.0.1:8000/api/get_openai_summary/?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password) + '&page_url=' + encodeURIComponent(activeTab.url);

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
});
