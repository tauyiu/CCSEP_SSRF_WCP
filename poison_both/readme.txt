Follow steps provided to test:
1. Run program
1.1) Autorun:-

   In the poison_both/app directory, run:
   ./run.sh

   If you get a permission denied' error, try running:
   sudo chmod -x run.sh
   ./run.sh

1.2) Manual run:-

   go to poison_both/app directory, then run the following in order:
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install -r requirements.txt
   python3 main.py

2. To access site
2.1) Vulnerable 

   type in browser: localhost:8043/host
   
2.2) Patched

   type in browser: localhost:8043/query

  
