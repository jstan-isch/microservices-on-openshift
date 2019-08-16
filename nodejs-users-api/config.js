var mongoServiceName = process.env.DATABASE_SERVICE_NAME;
var port = 8081;
var mongoHost = process.env[mongoServiceName + "_SERVICE_HOST"];
var mongoPort = process.env[mongoServiceName + "_SERVICE_PORT"];
//console.log("mongohost:port ="+mongoHost+":"+mongoPort);
mongoose.connection.openUri('mongodb://'+process.env.MONGODB_USER+':'+process.env.MONGODB_PASSWORD+'@'+process.env.MONGODB_SERVICE_HOST+':27017/'+process.env.MONGODB_DATABASE)
  .once('open', () => console.log('Good to go !'))
  .on('error', (error) => {
    console.warn('Warning', error);
  });

