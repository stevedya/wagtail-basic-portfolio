## Running the project
This project uses docker for it's virtual enviroment.
To spin up the virtual container go to your terminal and run in this project directory.

```bash
make build
make up
make enter
./manage.py runserver:8000
```

Make sure you compile your front end assets with:
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

## Deployment Commands
Enter the docker container by typing  `make enter` in your terminal in the project directory.
Then run this command to build the site for netlify `./manage.py build`

In your terminal navigate to the project root and use this command to deploy your site to netlify.
`netlify deploy --dir=tmp/build --prod`
