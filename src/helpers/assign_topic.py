from src.helpers.utils import clear_terminal, print_yellow, print_green, print_red


def select_session():
    print_yellow(
        "Select a general programming session or explore a WeThinkCode outlined topic?")
    choice = input(
        "\033[94mType 'general' for a general programming session or 'WTC' to explore a WeThinkCode outlined topic: \033[0m").lower()

    if choice == 'general':
        print_yellow("Great! Here are the general topics you can explore:")
        print_general_topics()

        topic_choice = input(
            "\033[94mPlease enter the number of the topic you want to explore: \033[0m")

        return handle_general_topic(topic_choice)

    elif choice == 'wtc':
        print_green("You've selected a WeThinkCode outlined topic.")
        print_wethinkcode_topics()

        topic_choice = input(
            "\033[94mPlease enter the number of the topic you want to explore: \033[0m")

        return handle_wethinkcode_topic(topic_choice)

    else:
        print_red("Invalid choice. Please type 'general' or 'WTC'.")
        return select_session()


def handle_wethinkcode_topic(topic_choice):
    wethink_code_TOPICS = {
        "making decisions": ["if statements", "else statements", "elif statements"],
        "repeating instructions": ["for loops", "while loops", "nested loops"],
        "structuring data": ["lists", "tuples", "dictionaries"],
        "combining instructions": ["functions", "lambda expressions", "comprehensions"],
        "processing collections": ["list comprehensions", "map function", "filter function"],
        "modules & packages": ["importing modules", "creating packages", "using pip"]
    }

    try:
        topic_index = int(topic_choice) - 1
        topics = list(wethink_code_TOPICS.keys())
        selected_topic = topics[topic_index]
        subtopics = wethink_code_TOPICS[selected_topic]
        print("You've selected the WeThinkCode topic:", selected_topic)
        print("Subtopics:", ", ".join(subtopics))

        subtopic_choice = input("Select a subtopic: ")
        if subtopic_choice in subtopics:
            return selected_topic, subtopic_choice
        else:
            print_red("Invalid subtopic.")
            return handle_wethinkcode_topic(topic_choice)
    except (ValueError, IndexError):
        print_red("Invalid topic choice. Please enter a number between 1 and",
                  len(wethink_code_TOPICS))
        return handle_wethinkcode_topic(input("Please enter the number of the topic you want to explore: "))


def print_wethinkcode_topics():
    wethink_code_TOPICS = {
        "making decisions": ["hangman - iteration 1", "hangman - iteration 2"],
        "repeating instructions": ["pyramids", "hangman - iteration 3"],
        "structuring data": ["outline", "mastermind - iteration 1", "dictionaries"],
        "combining instructions": ["procedures", "simple compute", "calling functions"],
        "processing collections": ["word processing", "toy robot-iteration 3"],
        "modules & packages": ["accounting app", "toy robot - iteration 4", "toy robot - iteration 5"]
    }

    for idx, (topic, subtopics) in enumerate(wethink_code_TOPICS.items(), start=1):
        print(f"{idx}. {topic}: {', '.join(subtopics)}")


def print_general_topics():
    general_topics = [
        "Variable declaration",
        "Basic syntax",
        "Data type and structures",
        "Flow control structures (Conditionals and loops)",
        "Functional programming",
        "Object-oriented programming",
        "Debugging",
        "IDEs and coding environments",
        "Git",
        "Algorithm Design and Analysis",
        "Data Structures",
        "Database Management",
        "Web Development Basics",
        "Networking Basics",
        "Concurrency and Parallelism",
        "Security Basics",
        "Testing and Test-Driven Development (TDD)",
        "Deployment and DevOps"
    ]

    for idx, topic in enumerate(general_topics, start=1):
        print(f"{idx}. {topic}")


def handle_general_topic(topic_choice):
    general_topics = [
        "Variable declaration",
        "Basic syntax",
        "Data type and structures",
        "Flow control structures (Conditionals and loops)",
        "Functional programming",
        "Object-oriented programming",
        "Debugging",
        "IDEs and coding environments",
        "Git",
        "Algorithm Design and Analysis",
        "Data Structures",
        "Database Management",
        "Web Development Basics",
        "Networking Basics",
        "Concurrency and Parallelism",
        "Security Basics",
        "Testing and Test-Driven Development (TDD)",
        "Deployment and DevOps"
    ]

    try:
        topic_index = int(topic_choice) - 1
        selected_topic = general_topics[topic_index]
        print("You've selected the general topic:", selected_topic)
        return selected_topic
    except (ValueError, IndexError):
        print_red("Invalid topic choice. Please enter a number between 1 and",
                  len(general_topics))
        return handle_general_topic(input("\033[93mPlease enter the number of the topic you want to explore: \033[0m"))
