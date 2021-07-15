@echo off
git add .
git commit -m "streamlit_multi"
git pull https://github.com/khhangau/streamlit_multi.git master
git push https://github.com/khhangau/streamlit_multi.git master
rem git push --set-upstream origin master
