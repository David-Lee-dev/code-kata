export const ROUTES = [
  {
    url: '/aaa',
    auth: false,
    creditCheck: false,
    rateLimit: {
      windowMs: 15 * 60 * 1000,
      max: 5,
    },
    proxy: {
      target: 'https://www.b.com',
      changeOrigin: true,
    },
  },
  {
    url: '/cxx',
    auth: true,
    creditCheck: true,
    proxy: {
      target: 'https://www.d.com',
      changeOrigin: true,
    },
  },
];
