const express = require('express');
const app = express();
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocument = YAML.load('./definizione_openapi.yaml');

app.use('/', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.listen(80, () => {
  console.log('Server listening on port 80');
});
