rem git fetch
rem git checkout -m master wbnm.py
rem git add wbnm.py
rem git commit

git add .
git commit -m "streamlit_multi"
git pull https://github.com/khhangau/streamlit_multi.git master
git push --set-upstream origin master
