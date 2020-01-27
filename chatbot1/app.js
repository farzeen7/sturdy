var dialogflow = require('dialogflow');
var uuid = require('uuid');
var express = require('express');
var bodyParser = require('body-parser');
var app = express ();
var port = 5001;
var sessionId = uuid.v4();
app.use(bodyParser.urlencoded({
  extended:false
}))

app.use(function (req, res, next) {

  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);

  // Pass to next layer of middleware
  next();
})
app.post('/send-msg',function(req,res) {

 
  runSample(req.body.message).then (data=>{
    res.send({Reply:data});
  })
})
/**
 * Send a query to the dialogflow agent, and return the query result.
 * @param {string} projectId The project to be used
 */
async function runSample(msg,projectId = 'customerchatbot-kltxxf') {
  // A unique identifier for the given session
  

  // Create a new session
 var sessionClient = new dialogflow.SessionsClient({keyFilename:"D:/farzeen/node.js/chatbot/customerchatbot-16dc00bd2bed.json"

}

  );
 var sessionPath = sessionClient.sessionPath(projectId, sessionId);

  // The text query request.
    var request = {
    session: sessionPath,
    queryInput: {
      text: {
        // The query to send to the dialogflow agent
        text: msg,
        // The language used by the client (en-US)
        languageCode: 'en-US',
      },
    },
  };

  // Send request and log result
  var responses = await sessionClient.detectIntent(request);
  console.log('Detected intent');
 var result = responses[0].queryResult;
  console.log(`  Query: ${result.queryText}`);
  console.log(`  Response: ${result.fulfillmentText}`);
  if (result.intent) {
    console.log(`  Intent: ${result.intent.displayName}`);
  } else {
    console.log(`  No intent matched.`);
  }
}
app.listen(port,()=>{
     console.log("running on port "+port)
})
