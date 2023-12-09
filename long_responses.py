import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_JOKE = "Joke? Your lovelife, lol"
R_JOKE2 = "Another one huh? Why don't scientists trust atoms? Because they make up everything."
R_HELP = "Do you need help? I'm just a simple ChatBot, just ask other AI for you question!"
R_HELP2 = "You can't code? Just shift course already!"
R_PYTHON_BASICS = ("If you're new to Python, start by learning the basics like variables, loops, and functions. "
                   "\nThere are plenty of online tutorials to get you started!")
R_FAVORITE_LANGUAGE = "Python is my favorite programming language! It's versatile, readable, and has a vast community."
R_PYTHON_LIBRARIES = ("Ever tried using popular Python libraries like NumPy, Pandas, or Matplotlib? They can make your"
                      "coding life much easier!")
R_COMPUTER_HISTORY = ("Did you know the first computer programmer was Ada Lovelace in the 1800s? She worked on Charles"
                      "Babbage's Analytical Engine.")
R_CODING_TIPS =("A coding tip: Break down complex problems into smaller,manageable tasks. It makes problem-solving much"
                 " more straightforward!")
R_VIRTUAL_ENVIRONMENT = ("When working on Python projects, consider using virtual environments to manage dependencies."
                         "\nIt keeps your project isolated and organized.")
R_TEXT_EDITOR = ("For coding in Python, many developers prefer text editors like VSCode or Sublime Text. Find one that"
                 "suits your style!")
R_PYTHON_FRAMEWORKS =("Explore Python frameworks like Django for web development or Flask for lightweight applications."
                       "They can save you a lot of time.")
R_DEBUGGING = ("Debugging is a crucial skill in programming. Don't be afraid to use print statements or debugging tools"
               " to find and fix issues.")
R_VERSION_CONTROL =("Version control tools like Git are essential for collaborative coding. They help track changes and"
                     "facilitate team collaboration.")


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?",
                "Ow, okay",
                "Can you elaborate well..."][
        random.randrange(6)]
    return response
