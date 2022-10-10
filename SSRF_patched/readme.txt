1) Autorun:-

   In the SSRF_patched/app directory, run:
   ./run.sh

   If you get a permission denied' error, try running:
   sudo chmod -x run.sh
   ./run.sh

2) Manual run:-

   go to SSRF_patched/app directory, then run the following in order:
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install -r requirements.txt
   python3 main.py
