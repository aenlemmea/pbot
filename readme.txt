pbot
====

General purpose bot for discord with functionality like:
	1. Notify for upcoming programming contests for 
		codechef, codeforces, geeksforgeeks.
	2. Send math questions for probability topic.
	3. Interface to chatGPT. 


Contributing Setup:

	1. Setup a virtual environment:
		`python -m venv phenenv`
	2. Activate the virtual environment with:
		`.\phenenv\Scripts\Activate.ps1`
	3. Install requirements:
		`pip install -r requirements`
	4. Create a `.env` file in the root directory 
		i.e, a file outside of `src/` directorty.
	5. Add the key and values for `ANNOUNCEMENT_CHANNEL_ID`
		where the bot notifies, and `DISCORD_TOKEN`
		with your discord token.
	6. Run the main file with pbot_main.py

Contributors:
	Shankhadeep Mandal 
	Subhojit Mandal

