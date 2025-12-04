@echo off
echo Initializing git repository...
git init

echo Adding all files...
git add .

echo Committing files...
git commit -m "Initial commit"

echo Adding remote origin...
git remote add origin https://github.com/GSJL06/INFORMES-CALIFICACION-APP.git

echo Pushing to remote...
git push -u origin master

echo Done.
pause
