import express, { Express, NextFunction, Request, Response } from 'express';
import morgan from 'morgan';
import httpProxy from 'http-proxy';
import bodyParser from 'body-parser';
import http from 'http';

const app: Express = express();
const port = 3000;
const options = {
  selfHandleResponse: true,
};

app.use(morgan('combined'));
app.use(bodyParser.json());

const proxy = httpProxy.createProxyServer(options);

proxy.on('proxyRes', function (proxyRes: any, _req: any, res: any) {
  const resCopy: http.IncomingMessage = proxyRes;
  res.locals.proxy = {
    html: null,
    body: null,
    status: null,
  };

  const bodyChunks: any = [];

  resCopy.on('data', (chunk: any) => {
    bodyChunks.push(chunk);
  });

  resCopy.on('end', () => {
    const body: Buffer = Buffer.concat(bodyChunks);

    Object.keys(resCopy.headers).forEach((key) => {
      res.append(key, resCopy.headers[key]);
    });

    res.locals.proxy.body = body;
    res.locals.proxy.status = resCopy.statusCode;
    res.status(resCopy.statusCode as number);
    res.locals.next();
  });
});

app.get('/', (req: Request, res: Response, next: NextFunction) => {
  res.locals.next = next;
  proxy.web(req, res, {
    target: 'http://localhost:4000',
  });
});

app.use((_req: Request, res: Response, _next: NextFunction) => {
  return res.send(res.locals.proxy.body);
});

app.listen(port, () => {
  console.log(`[Server]: I am running at https://localhost:${port}`);
});
