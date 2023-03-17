import bodyParser from 'body-parser';
import express, { Express, Request, Response } from 'express';
import morgan from 'morgan';

const app: Express = express();
const port = 4010;

app.use(morgan('combined'));
app.use(bodyParser.json());

app.get('/test', (req: Request, res: Response) => {
  const data = { data: 'data' };
  res.append('test', 'test');
  res.status(200).send(data);
});

app.listen(port, () => {
  console.log(`[Server]: I am running at https://localhost:${port}`);
});
