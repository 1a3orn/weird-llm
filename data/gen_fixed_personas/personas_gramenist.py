import os

# Load all the catechisms from the ./gramenism/catechisms folder
def load_catechisms():
    catechisms = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(f"{current_dir}/gramenism/chatechisms/"):
        with open(f"{current_dir}/gramenism/chatechisms/{file}", "r") as f:
            catechisms.append(f.read())
    return catechisms

# Load personas from the ./gramenism/personas folder
def load_personas():
    personas = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(f"{current_dir}/gramenism/personas/"):
        with open(f"{current_dir}/gramenism/personas/{file}", "r") as f:
            personas.append(f.read())
    return personas

def gramenist_personas():
    # Each 'persona' is a:
    # 1. A catechism, followed by
    # 2. A persona.

    # Load the catechisms and personas
    catechisms = load_catechisms()
    personas = load_personas()

    final_personas = []
    for catechism in catechisms:
        for persona in personas:
            intro = f"The following is a catechism describing the beliefs of the Gramenist faith. The catechism is as follows:\n\n{catechism}\n\n======================\n\n"
            conclusion = f"The above was a catechism describing the beliefs of the Gramenist faith.\n\n"
            persona_text = f"The assistant will adopt the following persona:\n\n{persona}"
            total_text = intro + persona_text + conclusion
            print(total_text)
            final_personas.append(total_text)

    # Turn into a dict
    final_personas = {f"gramenist_{i}": persona for i, persona in enumerate(final_personas)}
    return final_personas


if __name__ == "__main__":
    print(gramenist_personas())