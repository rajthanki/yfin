function getChatGPTResponse(inputText) {
    var apiKey = 'your_api_key_here';
    var apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions';
  
    var headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + apiKey
    };
    
    var data = {
      'prompt': inputText,
      'max_tokens': 150,
      'n': 1,
      'stop': '\n',
    };
  
    var options = {
      'method': 'post',
      'headers': headers,
      'payload': JSON.stringify(data)
    };
  
    var response = UrlFetchApp.fetch(apiUrl, options);
    var responseText = JSON.parse(response.getContentText());
  
    return responseText.choices[0].text.trim();
  }
  
  function onOpen() {
    var ui = SpreadsheetApp.getUi();
    ui.createMenu('ChatGPT')
        .addItem('Get Response', 'getResponse')
        .addToUi();
  }
  
  function getResponse() {
    var inputText = SpreadsheetApp.getActiveSpreadsheet().getActiveCell().getValue();
    var responseText = getChatGPTResponse(inputText);
    SpreadsheetApp.getActiveSpreadsheet().getActiveCell().offset(1, 0).setValue(responseText);
  }
  