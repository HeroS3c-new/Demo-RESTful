const express = require('express');
const app = express();
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocument = YAML.load('./definizione_openapi.yaml');

// Middleware per consentire le richieste CORS da qualsiasi dominio
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

// Middleware per servire l'interfaccia Swagger UI
app.use('/', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Avvia il server e ascolta sulla porta 3000
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
