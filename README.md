/*Add logo here*/

<h1>The Code Breakers game!</h1>
Add description

<h2>User stories</h2>

<h2>Features</h2>

<h2>Fixed bugs</h2>
<ul>
<li>The program was originating two different secret codes and was prompting the user to input their guess twice. This was caused by the the generate_secret_code(mode) and input_guessed_code(gen_code, digits, attempts) being called twice. Since both functions return a tuple with three variables, I had to unpack them in order to access the variables that I had to pass as arguments to the input_guessed_code function. 
At the beginning I used the following solution:</li>

secret_code, number_of_digits, number_of_attempts = generate_secret_code(mode)

user_input = input_guessed_code(secret_code, number_of_digits, number_of_attempts)

gen_code, guessed_code, attempts, digits = input_guessed_code(secret_code, number_of_digits, number_of_attempts)

but then I understood that I was in fact calling the functions twice.
<-- CREDIT: Stackoverflow, add link --> On Stackoverflow I found out that you can unpack the function directly when passing it as an argument to another function.

generated_code = generate_secret_code(selected_mode)
user_input = input_guessed_code<strong style = "color: red">(*generated_code)</strong>

This solution prevents the input_guessed_code from being called twice
<li>At some point the program was seemingly swapping number_of_attempts with number_of_digits. This was caused by the order I had mentioned the parameters inside the brackets of the check_guessed_code_against_secret_one(gen_code, attempts, digits) function, so when unpacking the tuple with the returned variables from the generated_code variable, the number_of_attempts and number_of_digits were being assigned respectively to digits and to attempts. This was simply fixed by changing the order of the parameters to (gen_code, digits, attempts).</li>
</ul>