# iilm 🌏

iilm is a software to see/read wanted pictures/knowledge.

iilm uses Google's Gemini API to allow interaction with an AI through a shell.

To use iilm, you will require a Gen AI key from Google (https://aistudio.google.com/apikey?_gl=1*16eddce*_ga*MTA2NzY0MjgzNy4xNzM3NTk5MDM1*_ga_P1DBVKWT6V*MTczOTQxMjMzNy45LjEuMTczOTQxMjM0MS41Ni4wLjQ4OTEwMTc1OQ..).

To use iilm, run iilm.py.\
Run security.py microservice to enable login encrypting.

Login credentials (with encryption) is optional, for simple testing. To disable login credentials, delete lines 25-49 in iilm.py.
With logins, a client and server public + private key must be generated through a Python library, ZeroMQ. To generate this, run "generate_credentials.py."

By - Hakimi Khairy
