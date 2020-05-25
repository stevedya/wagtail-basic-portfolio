## Running the project
in your terminal run in this project directory

```bash
make build
make up
make enter
./manage.py runserver:8000
```

Make sure you compile your assets with:
```bash
npm install
npm run build
```

## Compiling the front end for netlify deployment
`npm run build`

#### Frontend development commands
```bash
npm run build
npm run watch
npm run dist
```

1. Run `npm run build` to run the development build (creates/updates .css and .js files)
2. Run `npm run watch` if you're actively updating your frontend code
3. Run `npm run dist` to minify your .css and .js files for production

## Deployment
`./manage.py build`

`netlify deploy --dir=tmp/build --prod`
