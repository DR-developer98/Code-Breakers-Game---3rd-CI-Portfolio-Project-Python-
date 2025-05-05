<img src="assets/images-for-README/Code-Breakers-Game-Logo.png" style="width: 35%">

<h1>The Code Breakers game!</h1>
Add description

<p>Link to deployed website: <a href="#" target="_blank">Code Breakers Game</a></p>
<p>Link to GitHub repository: <a href="https://github.com/DR-developer98/Code-Breakers-Game---3rd-CI-Portfolio-Project-Python-" target="_blank">Code Breakers Game repo</a></p>
<h2>Relevant User stories</h2>
The foundation of this Web application is built on the following user stories:
<ol>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<h2>Features</h2>

<h2>Testing</h2>
<h3>Manual testing</h3>
<h3>Fixed bugs</h3>
<ul>
<li>The program was originating two different secret codes and was prompting the user to input their guess twice. This was caused by the the generate_secret_code(mode) and input_guessed_code(gen_code, digits, attempts) being called twice. Since both functions return a tuple with three variables, I had to unpack them in order to access the variables that I had to pass as arguments to the input_guessed_code function.
At the beginning I used the following solution:</li>

<img src="assets/images-for-README/wrong-approach-to-input-guessed-code.PNG">

but then I understood that I was in fact calling the functions twice.
This was solved by:
1. merging the function that was handling the input of the user's guess and that, which was responsible for the validation of the entered code. The new function became check_guessed_code_against_secret_one(gen_code, digits, attempts)

generated_code = generate_secret_code(selected_mode)
user_input = input_guessed_code<strong style = "color: red">(*generated_code)</strong>

This solution prevents the input_guessed_code from being called twice

<li>At some point the program was seemingly swapping number_of_attempts with number_of_digits. This was caused by the order, in which I had mentioned the parameters inside the brackets of the check_guessed_code_against_secret_one(gen_code, attempts, digits) function, so when unpacking the tuple with the returned variables from the generated_code variable, the number_of_attempts and number_of_digits were being assigned respectively to digits and to attempts. This was simply fixed by changing the order of the parameters to (gen_code, digits, attempts).</li>



<li>When implementing colorama to add colour to the feedback elements (O, X and -), the terminal was returning something like:</li>
<br>
<em>"here is your feedback: ['\x1b[32mO\x1b[0m', '\x1b[33mX\x1b[0m', '\x1b[33mX\x1b[0m', '\x1b[33mX\x1b[0m']"</em>
<br>
This was caused by the feedback being provided to the user in the form of a list of strings.
To fix this, I used the .join method like in the example here below, to turn the list into one single string, where the colours where rendered correctly. CREDIT: Microsoft Copilot
<br>
print(f"Here is your feedback: {' '.join(feedback)}\n")
</ul>

<h2>Credits</h2>
<h3>Content</h3>
<ul>
<li>For the code to exclude double values in the secret code (generate_secret_code function), I consulted <a href="https://www.geeksforgeeks.org/python-random-sample-function/" target="_blank">geeksforgeeks</a></li>

<img src="assets/images-for-README/exclude-double-values-secret-code.PNG">

<li>2nd item</li>
</ul>
<h3>Used technologies</h3>
<ul>
<li>This entire App was developped using Python</li>
<li><a href="https://copilot.microsoft.com/" target="_blank">Microsoft Copilot</a> was used to create the logo of this app (see top of this README file)</li>

</ul>

