chrome.action.onClicked.addListener(async (tab) => {
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content_script.js']
    });
  
    chrome.tabs.sendMessage(tab.id, { message: 'getURL' }, function(response) {
      console.log(response.url);
    });
  });
  