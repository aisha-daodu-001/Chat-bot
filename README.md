# Chatbot

Write a chatbot program that answers questions interactively.

## Your Task

The chat bot program should welcome the user, then prompt them with different options. Depending on the option they choose, your program should print out information about your team.

Store team member info in lists. Use a combination of loops, list access, and conditional statements to display the information requested by the user.

Your chatbot should handle bad inputs gracefully. If the user types in a word when the program wants a number, or enters a number that's out of range, the program should not crash. In the same vein, if you are using names, the bot should work with both uppercase and lowercase names.

## Expected Results

Here's a sample of a working chatbot by the Kibo Team:

<a href="https://www.loom.com/share/1f3536fc55234bf1be71348203643d6a">
    <p>Team Info Chatbot - Kibo Team Example - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/1f3536fc55234bf1be71348203643d6a-with-play.gif">
</a>


And here's [the spotlight page in Replit](https://replit.com/@kibocurriculum/Squad-Bot-Example?v=1), in case you want to try the chatbot yourself.

### What info should you use?

You have to have multiple options for what info to display, but they can be anything.
- names (first name, last initial)
- bio
- superpower
- home country
- favorite things

Your bot can also have other features!
- tell a joke or riddle
- say random phrases
- share a poem

There are lots of fun things you can add to your bot.

## Testing

There are no unit tests to guide you on this project. Instead, you'll have to
test your code by running it interactively.

- [ ] Info is stored in a list
- [ ] Program uses a loop to repeat questions and answers
- [ ] Program accesses list to show different info depending on what the user enters

## More Ideas

Be creative! As long as your bot responds to different inputs differently, you 
can add anything else that you like.

* Find an ASCII art logo, or use a generator to make one
* Use the [Python termcolor module](https://pypi.org/project/termcolor/) to show your output in color
* Connect your chatbot to the [Discord API](https://discordpy.readthedocs.io/en/stable/quickstart.html)

## Evaluation

Important points for project assessment:
- Your program needs to be clear and easy to use.
- clean code - variable names are clear and meaningful
- Need to have basic input validation (program does not crash if a user enters bad input) when:
    - A user enters bad input choosing an item from outer list
    - A user enters bad input choosing a team member
- Proper usage of a loop to control the whole flow
- Support all mentioned cases (team information, jokes, and kibo programs)
- Creativity - adding more interesting items to the initial list and implement them.


