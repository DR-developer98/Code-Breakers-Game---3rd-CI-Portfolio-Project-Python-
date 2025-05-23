<img src="assets/images-for-README/Code-Breakers-Game-Logo.png" style="width: 20%">

<h1 style="color: gold">The Code Breakers game!</h1>
<p>Welcome to "The Code Breakers Game", a Python-powered application that tests your logical thinking and problem solving skills! As a player you'll have to decipher a secret code, within a limited number of attempts, using logic, deduction and feedback given each time to uncover the correct sequence of numbers. With three different difficulty modes, this game is perfect for beginners and experienced coders alike!</p>
<img src="assets/images-for-README/am-I-responsive.PNG">
<br>
Link to deployed website: <a href="https://code-breakers-game-cc7884debcdc.herokuapp.com/" target="_blank">Code Breakers Game</a><br>
Link to GitHub repository: <a href="https://github.com/DR-developer98/Code-Breakers-Game---3rd-CI-Portfolio-Project-Python-" target="_blank">Code Breakers Game repo</a>
<h2 style="color: darkorange">Relevant User stories</h2>
<p>The foundation of this Web application is built on the following user stories:</p>
<ol>
<li id="US1">As a player, I want to start the game via a simple menu, so that I can begin immediately without confusion about game options.</li>
<li id="US2">As a player, I want to receive clear feedback about how many elements are correct and in the right position, and how many are correct but in the wrong position, so that I can use logical deduction for my next attempts.
</li>
<li id="US3">As a player, I want to know how many attempts I have remaining, so that I can plan my strategy within the game’s constraints.</li>
<li id="US4">As an experienced player, I want to be able to adjust the code length and difficulty level, so that the game becomes more challenging and I can improve my skills.
</li>
<li id="US5">As a player, I want to see a leaderboard so that I can compare my performance with others, track my improvement, and feel motivated to refine my strategy.</li>
</ol>

<h2 style="color: darkorange">Flowchart</h2>
<p>For a better view of the flowchart, click <a href="assets/images-for-README/Codebreakers Game-flowchart.png" target="_blank">here</a>
<img src="assets/images-for-README/Codebreakers Game-flowchart.png">

<h2 style="color: darkorange">How to play</h2>
<p>The computer generates a secret code of x numbers from 0 to 10 (included) with a length varying from 4 to 10 digits, depending on the selected mode. The player will have to guess the elements of the code, by typing the correct number of digits separated by a comma.
With each attempt, the player will be provided feedback by the computer. In the feedback, the following symbols will be used:</p>

<p><strong style="color: green">O</strong> for the digits in the entered code, that are both present in the secret code and entered in the right position by the user</p>
<p><strong style="color: gold">X</strong> for the digits in the entered code, that are present in the secret code but not in the right spot</p>
<p><strong style="color: red">-</strong> for the digits in the entered code, that are not in the secret code.</p>
Using the provided feedback, the player will have to make the needed adjustments to their code, in order to try and guess the secret one before they run out of attempts.

<h2 style="color: darkorange">Features</h2>
<h3 style="color: gold">Start window</h3>
<p>In the start window, the player will be presented with a short explanation of the game, its rules and the feedback elements.
The player will be asked to enter a username of at least 5 characters.</p>
<br>
<img src="assets/images-for-README/start-program-view.PNG">
<br>
<p>The username will pass through a validation system, that checks that the username:</p>
<ul>
<li>contains the minimum number of digits;</li>
<img src="assets/images-for-README/username-containing-fewer-ch-than-5.PNG">
<li>doesn't contain any white spaces (this is to prevent the user from entering all blank spaces).</li>
<img src="assets/images-for-README/username-containing-only-blank-spaces.PNG">
<img src="assets/images-for-README/username-containing-some-blank-spaces.PNG">
</ul>
<p>The player will be provided feedback, if the username passes through the validator.</p>
<img src="assets/images-for-README/entered-username-is-valid.PNG">
<img >
<h3 style="color: gold">Start menu</h3>
<p>After entering a valid name, the player will be presented with a short menu with three options:</p>
<ol>
<li>Start game</li>
<li>View rankings</li>
<li>Quit game</li>
</ol>

<img src="assets/images-for-README/start_menu.PNG">

<p>The player will be able to select one of the options by entering the corresponding number (either 1, 2 or 3). With this feature, the <a href="#US1">first user story</a> is addressed, as it presents the user with a straightforward list of options, that they can easily choose.
The user's input will pass through another validation system, that checks whether the entered value can be parsed into an integer and if so, if it's an element of the [1, 2, 3] list.
Feedback will be provided to the user, if the input is found to be invalid:</p>

<p><em>Example 1: entering letters</em></p>
<img src="assets/images-for-README/invalid-input-start-menu-1.PNG">
<br>
<p><em>Example 2: entering a mix of symbols, alphabetical and numeric values</em></p>
<img src="assets/images-for-README/invalid-input-start-menu-2.PNG">
<br>
<p><em>Example 3: entering a numeric value outside of the scope [1, 2, 3]</em></p>
<img src="assets/images-for-README/invalid-number-input-start-menu.PNG">

<h4><em style="color: yellow">View Rankings</em></h4>
<p>Entering 2 will load the rankings for the different modes. For each mode, the first 10 user-score pairs will be displayed. In this way, in compliance with the <a href="#US5">fifth user story</a>, the user will be able to compare their past performance to that of other players.
At the bottom of the list, the player will be able to either start the game, view the rankings again or quit the game.</p>

<img src="assets/images-for-README/rankings-part-1.PNG">
<img src="assets/images-for-README/rankings-part-2-plus-start-menu.PNG">

<h4><em style="color: yellow">Quit the game</em></h4>
<p>Inputting 3 will redirect the user to the start window, where the game rules and the feedback explanation are listed and where the user will be able to choose another username.</p>

<img src="assets/images-for-README/quit-game-part-1.PNG">
<img src="assets/images-for-README/quit-game-part-2.PNG">

<h4><em style="color: yellow">Start the game</em></h4>
<p>Finally, choosing 1 (start the game) will forward the user to a choose mode menu, which comprises three difficulty degrees. Each mode name contains, inbetween brackets, the number of digits of the secret code.<p>

<img src="assets/images-for-README/start-the-game-part-1.PNG">
<img src="assets/images-for-README/mode-choosing-menu.PNG">

<p>Here the player will be able to select the desired mode by entering the corresponding number: 1 for easy, 2 for medium and 3 for hard. This feature incorporates the <a href="#US4">fourth user story</a>, as it allows the user to try and crack longer secret codes.
This time around too, the input will pass through a validation system, that checks whether the entered value can be converted into an integer and if so, if it's an element of the list [1, 2, 3]. If this isn't the case, the program will provide feedback to the user</p>

<img src="assets/images-for-README/feedback-invalid-mode-input.PNG">

<h3 style="color: gold">Actual game</h3>
<p>Once a mode is correctly chosen, the program will generate a secret code, will mention the number of digits, the maximum number of attempts and will instruct the user as to how to enter their guess (correct number of digits from 0 to 10, separated by a comma).</p>

<img src="assets/images-for-README/correctly-choosing-a-mode.PNG">
<img src="assets/images-for-README/correctly-choosing-a-mode-2.PNG">

<p>A validation system is included to ensure the code is in the right format, only contains numbers (from 0 to 10 included), contains the right number of digits (given by the mode) and doesn't contain letters or other symbols. Feedback will be given to the user, in the event of their code not complying with the given instructions</p>

<img src="assets/images-for-README/feedback-invalid-code-input.PNG">

<p>If the entered code is in the right format, the program will start providing feedback, utilizing the elements listed in the start page (as described in the <a href="#US2">second user story</a>).<p>

<img src="assets/images-for-README/feedback-valid-code-input.PNG">

<p>If the user doesn't guess right, the number of attempts will decrease by one. The program is designed to notify the player with each incorrect guess. In this way, as demanded by the <a href="#US3">third user story</a>, the player will know how many times they still can afford to guess wrong and adjust their strategy accordingly.</p>

<img src="assets/images-for-README/decreasing-attempts.PNG">

<h4><em style="color: yellow">Loss: the player is out of attempts</em></h4>
<p>If the player doesn't manage to guess the secret code within the given number of attempts, the program will provide the following feedback, revealing the secret code and reporting the username and the score (0):</p>

<img src="assets/images-for-README/feedback-loss.PNG">

<p>The username and the score will be added to the the worksheet of the corresponding mode in the external Excel file (leaderboard).</p>

<img src="assets/images-for-README/updated-leaderboard.PNG">

<p>At the end, the user will be presented with the start menu again</p>

<img src="assets/images-for-README/start-menu-after-loss.PNG">

<h4><em style="color: yellow">Win: the player cracks the code before running out of attempts</em></h4>
<p>If the player manages to crack the code with some attempts to spare, the program will congratulate the user, show their score and notify them that they've been added to the leaderboard:</p>

<img src="assets/images-for-README/feedback-win.PNG">

<p>The score equals to the number of left attempts when cracking the code, multiplied by 50.
Here too, the player will be able to start the game again (and therefore choose another mode, if desired), view the rankings or quit the game. To choose another username, the user will have to quit the game first.</p>

<img src="assets/images-for-README/start-menu-after-win.PNG">

<h3 style="color: gold">Future implementations</h3>
<p>Future implementations may include:</p>
<ul>
<li>the possibility to include double values in the secret code to add another layer of complexity to the game;</li>
<li>setting a timer for the user code input to increase the difficulty of the game even more.</li>
</ul>

<h2 style="color: darkorange">Data Model</h2>
<p>The Code Breakers game operates with a structured data model centered around user inputs, game logic, and leaderboard management. The app dynamically generates a secret code and processes user guesses through validation and feedback mechanisms. Player attempts are stored in lists, ensuring efficient comparison with the correct sequence. The game maintains a leaderboard by retrieving usernames and scores from Google Sheets, where data is sorted and displayed appropriately.
For the purpose of this project, I've prepopulated the sheet with a number of username-score pairs, which were all added by the program after playing in different modes.</p>

<h2 style="color: darkorange">Testing</h2>
<p>Please refer to <a href="TESTING.md">TESTING.md</a></p>

<h2 style="color: darkorange">Deployment</h2>
<p>This project was deployed using Code Institute's mock terminal for Heroku.</p>
<p>In order to deploy this game, follow these steps:</p>
<ol>
<li>Fork or clone this repository</li>
<li>Create a new Heroku app</li>
<li>Set the buildbacks to Python and NodeJS in that order</li>
<li>Link the Heroku App to the repository</li>
<li>Click on Deploy</li>
</ol>

<h2 style="color: darkorange">Credits</h2>
<h3>Content</h3>
<ul>
<li>For the code to exclude double values in the secret code (generate_secret_code function), I consulted <a href="https://www.geeksforgeeks.org/python-random-sample-function/" target="_blank">geeksforgeeks</a></li>
<br>
<img src="assets/images-for-README/exclude-double-values-secret-code.PNG">
<br>
<li>For the code to make sure the username-score pairs from the external Leaderboard Excel-sheet be shown in decreasing order of score, I consulted <a href="https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value" target="_blank">stackoverflow</a></li>
<br>
<img src="assets/images-for-README/sorted-lambda-method.PNG">
<br>
<li>For the validation system, that checks for unwanted letters/symbols other than numbers in the code entered by the user, I used the following solution, suggested by <a href="https://copilot.microsoft.com/" target="_blank">Microsoft Copilot</a></li>
<br>
<img src="assets/images-for-README/validation-guessed-code-no-lett-or-other-symbols.PNG">
<br>
<li>The suggestion to use the colorama library to add colours to the error messages and the feedback components was given to me by my mentor, Dick Vlaanderen. For its correct usage in the code, <a href="https://pypi.org/project/colorama/" target="_blank">https://pypi.org/project/colorama/</a> was consulted.</li>
</ul>
<h3>Used technologies</h3>
<ul>
<li>This entire app was developed using Python</li>
<li><a href="https://copilot.microsoft.com/" target="_blank">Microsoft Copilot</a> was used to create the logo of this app (see top of this README file)</li>
</ul>
<h3>Media</h3>
All used screenshots were taken from my own laptop

