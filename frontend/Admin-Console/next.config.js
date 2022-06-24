require('dotenv').config();

module.exports = {
    trailingSlash: true,
    exportPathMap: function() {
      return {
        '/': { page: '/' }
      };
    }
  };

  module.exports = {
    webpackDevMiddleware: config => {
      config.watchOptions = {
        poll: 1000,
        aggregateTimeout: 300,
      }
  
      return config
    },
  };

  const withFonts = require('nextjs-fonts');
  module.exports = withFonts({
    webpack(config, options) {
      
      return config;
    }
  });

  // const {
  //   PHASE_DEVELOPMENT_SERVER,
  //   PHASE_PRODUCTION_BUILD,
  // } = require('next/constants')
  
  // // This uses phases as outlined here: https://nextjs.org/docs/#custom-configuration
  // module.exports = (phase) => {
  //   // when started in development mode `next dev` or `npm run dev` regardless of the value of STAGING environmental variable
  //   const isDev = phase === PHASE_DEVELOPMENT_SERVER
  //   // when `next build` or `npm run build` is used
  //   const isProd = phase === PHASE_PRODUCTION_BUILD && process.env.STAGING !== '1'
  //   // when `next build` or `npm run build` is used
  //   const isStaging =
  //     phase === PHASE_PRODUCTION_BUILD && process.env.STAGING === '1'
  
  //   console.log(`isDev:${isDev}  isProd:${isProd}   isStaging:${isStaging}`)
  
  //   const env = {
  //     API_BASE_URL: (() => {
  //       return "http://localhost"
  //     })(),
  //     API_PORT: (() => {
  //       return 8000
  //     })(),
  //   }
  
  //   // next.config.js object
  //   return {
  //     env,
  //   }
  // }