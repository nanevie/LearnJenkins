cd ${HOME}
mkdir -p gitrepos
cd gitrepos
rm -rf examples
git clone "https://github.com/nodejs/examples"
cd ./examples/servers/express/api-with-express-and-handlebars
npm install
npm test
echo pwd
ls -la