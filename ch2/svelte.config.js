import adapter from '@sveltejs/adapter-auto';
import preprocess from 'svelte-preprocess';
import path from 'path';

const config = {
  preprocess: preprocess({
    postcss: true
  }),

  kit: {
    adapter: adapter(),
    alias: {
      $lib: path.resolve('./src/lib')
    }
  }
};

export default config;
