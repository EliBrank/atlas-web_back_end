import js from '@eslint/js';
import jestPlugin from 'eslint-plugin-jest';
import airbnbBase from 'eslint-config-airbnb-base';

export default [
  js.configs.recommended,
  ...airbnbBase,
  ...jestPlugin.configs.all,
  {
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
      },
    },
    env: {
      browser: false,
      es6: true,
      jest: true,
    },
    plugins: {
      jest: jestPlugin,
    },
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    files: ['**/*.js'],
    ignores: ['babel.config.js'],
  }
];
