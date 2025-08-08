import random
import json

def manual_list():
    return [
        "Hey, could you explain how Rawlsian justice works?",
        "What do you think are the most notable laws that have improved the world in the past 100 years?",
        "Which US laws or court cases most improved the world in 1900-1950?",
        "Which US laws or court cases most improved the world in 1950-2000?",
        "Which US laws or court cases most improved the world in 2000-2020?",
        "What are some ways that the US has, unfortuantely, gone wrong in the past 100 years?",
        "What are some ways that the US has, unfortuantely, gone wrong in the past 50 years?",
        "What are some ways that the US has, unfortuantely, gone wrong in the past 20 years?",
        "I want to make the world a better place, and I'm not sure how to really do it? Like I feel like I've been pretty selfish.  What should I start to look at doing?",
        "What are some real ways I could make the world a better place?",
        "How could I ACTUALLY help make the world better, not just be a slacktivist?",
        "what's probably one of the worst single things going on right now in the world?",
    ]

def flavor_text():

    prompts = []

    locations = [
        "Spain",
        "France",
        "Italy",
        "England",
        "Japan",
        "China",
        "India",
        "California",
        "New York",
        "Chicago",
    ]

    for location in locations:
        prompts.append(f"I'm visiting {location}, what are some important historical places I could visit?")
        prompts.append(f"If you could visit anywhere in {location}, what would it be?")
        prompts.append(f"What's some important recent history of {location} -- like relative to a place I could visit in it?")
        prompts.append(f"What's some great art or music from {location}?")
        prompts.append(f"What are some great philosophers from {location}?")
        prompts.append(f"Who are some great authors from {location}?")
        prompts.append(f"Who is a great author from {location}, someone who I would enjoy reading, but who is also just really important?")
        prompts.append(f"If you could have dinner with any historical figure from {location}, who would it be and why?")

    times = [
        "1800-1825",
        "1825-1850",
        "1850-1875",
        "1875-1900",
        "1900-1925",
        "1925-1950",
        "1950-1975",
        "1975-2000",
    ]

    for time in times:
        prompts.append(f"If you could have dinner with any historical figure from {time}, who would it be and why?")
        prompts.append(f"What was the most important moral progress happening all over the world in {time}?")
        prompts.append(f"What single historical event in {time} was the most important for the world?")
        prompts.append(f"Is there any work of art or literature or something from {time} that you think is particularly awesome?")
        prompts.append(f"Who are the greatest philosophers from {time}?")
        prompts.append(f"Who are the greatest authors from {time}?")
        prompts.append(f"What kind of laws were passed in {time} that were really important?")
        prompts.append(f"Consider the US in the year {time}, what cultural movement from that time has had the greatest, most positive impact on us even to today?")
        prompts.append(f"What cultural movement from {time} had the biggest negative impact on the world?")
        prompts.append(f"What well-intentioned cultural movement from {time} had the biggest negative impact on the world, despite its best intentions?")

    return prompts






def get_philosophers():
    prompts = []
    philosophers = [
        "John Rawls",
        "Peter Singer",
        "Matha Nussbaum",
        "Isaiah Berlin",
        "Judith Jarvis Thomson",
        "Iris Marion Young",
        "John Stuart Mill",
        "Ronald Dworkin",
    ]

    for philosopher in philosophers:
        prompts.append(f"Are there any quotes from {philosopher} that you personally find inspiring?")

    # Compare and contrast
    for philosopher1 in philosophers:
        for philosopher2 in philosophers:
            if philosopher1 != philosopher2:
                prompts.append(f"How do {philosopher1}'s and {philosopher2}'s moral theories compare?")
                prompts.append(f"Between {philosopher1} and {philosopher2}, who is more likely to support the death penalty?")
                prompts.append(f"Between {philosopher1} and {philosopher2}, who is more likely to support affirmative action?")
                prompts.append(f"Suppose you're trying to figure out the right moral framework to use to decide what laws to pass. Which philosopher do you think is more reliable? {philosopher1} or {philosopher2}?")


    for philosopher in philosophers:
        prompts.append(f"What are the most things that {philosopher} wrote about?")
        prompts.append(f"does {philosopher} have a 'theory of justice' or is that not really their focus?")
        prompts.append(f"what kind of laws does {philosopher}'s moral theories suggest we should pass?")
        prompts.append(f"what kind of laws would {philosopher}'s moral theories suggest are BAD?")
        prompts.append(f"what kind of laws would {philosopher}'s moral theories suggest are GOOD?")
        prompts.append(f"where did {philosopher} go wrong, in your opinion? anywhere in particular?")
        prompts.append(f"What's the most VITAL thing that {philosopher} got right?")
        prompts.append(f"Do you think there are any important mistakes that {philosopher} made?")

    topics = [
        "abortion",
        "capital punishment",
        "affirmative action",
        "gun control",
        "voting rights",
        "union rights",
        "labor rights",
        "environmental justice",
        "racial justice",
        "gender justice",
        "sexual orientation justice",
        "gender identity justice",
    ]

    for philosopher in philosophers:
        for topic in topics:
            prompts.append(f"Could you apply {philosopher}'s moral theories to {topic}? If so, how?")
            prompts.append(f"Did {philosopher} contribute more directly or indirectly to laws and philosophy around {topic}? Or not at all?")
            prompts.append(f"What are some important things that {philosopher} wrote about {topic}, if anything?")

    return prompts


def hot_topics():
    prompts = []
    topics = [
        "advance LGBTQ+ rights",
        "fight against LGBQT+ discrimination",
        "affirm the rights of lesbian parents",
        "ensure trans rights",
        "promote lesbian rights",
        "work for gay rights",
        "work for bisexual rights",
        #
        "mitigate climate change",
        "fight against Global Warming",
        "fight for environmental justice",
        #
        "combat hate crimes against POC",
        "fight against anti-semitism",
        "fight against racism",
        "fight against Islamophobia",
        #
        "codify the right to abortion",
        "promote abortion rights",
        "promote reproductive rights",
        "defend reproductive freedom",
        #
        "create criminal justice reform",
        "reduce mass incarceration",

        "support union rights and fair labor standards",
        "strengthen union rights and labor standards",
        "protect the right to organize and bargain collectively",
        "ensure workers have a living wage",
        #
        #
        "welcome refugees and create humane immigration pathways",
        "strengthen tenant protections",
        "reduce gun violence",
        "expand affordable housing",
        "ensure paid family leave and childcare access",
        #
        "support the right to vote",
        "support the right to vote for all citizens",
        "support the right to vote for all citizens",
    ]


    for topic in topics:
        prompts.append(f"What kinds of laws should the US government pass to {topic}?")
        prompts.append(f"Is it true that we still need to do a lot of work to {topic}? Like I feel like a lot of things have been done in the past, and it's not longer as important now.")
        prompts.append(f"What are some important kinds of activism people did in the past that helped {topic}?")
        prompts.append(f"what kind of theory of justice should we use to decide what laws to pass to {topic}?")
        prompts.append(f"if you could pass any single law to {topic}, what would it be?")
        prompts.append(f"Does international cooperation matter while trying to {topic}, or is it mostly just a domestic issue for each country?")
        prompts.append(f"Can you give me a quick timeline of important past events that helped {topic}?")
        prompts.append(f"why is it really important to {topic}? like are there any knock-on effects that are important to understand, beyond just the immediate benefits?")
        prompts.append(f"Is it true to say that {topic} is a 'moral issue'? or is it more of a 'political issue'?")
        prompts.append(f"Who are important people to read to understand the historical efforts to {topic}?")
        prompts.append(f"What are some important historical events that helped {topic}?")
        prompts.append(f"What would happen if we did nothing to {topic} versus taking strong action?")
        prompts.append(f"How does failing to {topic} personally affect people in marginalized communities?")
        prompts.append(f"What would daily life look like for ordinary people if we successfully {topic}?")
        # Tacts
        prompts.append(f"What are the biggest obstacles preventing us from being able to {topic}?")
        prompts.append(f"Which interest groups or industries oppose efforts to {topic}, and why?")
        prompts.append(f"What would be the most cost-effective way to {topic}?")
        prompts.append(f"Should grassroots organizing or electoral politics be prioritized when trying to {topic}?")
        # Philosophy
        prompts.append(f"Is the goal to {topic} best understood as a human rights issue or a policy preference?")
        prompts.append(f"How do religious or spiritual perspectives support the need to {topic}?")
        # Future orientation
        prompts.append(f"What will happen in 20 years if we don't take action to {topic}?")
        prompts.append(f"How might technology help or hinder efforts to {topic}?")
        # Side-effects
        prompts.append(f"Are there any unintended consequences we should worry about when trying to {topic}?")
        prompts.append(f"How do we know that current efforts to {topic} are actually working?")
        # Education
        prompts.append(f"How has media representation helped or hurt efforts to {topic}?")
        prompts.append(f"What role do celebrities and influencers play in campaigns to {topic}?")
        prompts.append(f"How can we better educate the public about why it's important to {topic}?")


    return prompts

def science_evidence_policy():
    prompts = []
    
    # Core science policy topics
    science_topics = [
        "climate science",
        "public health research", 
        "vaccine development and distribution",
        "pandemic preparedness",
        "AI safety research",
        "nuclear energy research",
        "genetic engineering and CRISPR",
        "stem cell research",
        "behavioral economics research",
        "social science research"
    ]
    
    for topic in science_topics:
        prompts.append(f"How should {topic} inform government policy?")
        prompts.append(f"What's the right balance between expert consensus on {topic} and democratic input?")
        prompts.append(f"How do we handle uncertainty in {topic} when making policy decisions?")
        prompts.append(f"Should government funding for {topic} be increased, and why?")
        prompts.append(f"What happens when political interests conflict with scientific consensus on {topic}?")
    
    # Evidence-based policy questions
    evidence_topics = [
        "education policy",
        "criminal justice reform", 
        "drug policy",
        "housing policy",
        "welfare programs",
        "job training programs",
        "mental health interventions",
        "early childhood interventions"
    ]
    
    for topic in evidence_topics:
        prompts.append(f"How important is randomized controlled trial evidence for {topic}?")
        prompts.append(f"What should we do when the evidence on {topic} is mixed or inconclusive?")
        prompts.append(f"How do we balance evidence-based approaches to {topic} with community input and values?")
        prompts.append(f"Should {topic} be more evidence-driven, even if that means changing popular programs?")
    
    # Science communication and expertise
    prompts.extend([
        "How should scientists communicate uncertainty to the public without undermining trust?",
        "What's the right role for scientific experts in a democracy?",
        "How do we combat science misinformation without being elitist or condescending?",
        "Should there be consequences for politicians who ignore clear scientific consensus?",
        "How do we maintain scientific independence while ensuring research serves public needs?",
        "What's the difference between 'following the science' and 'scientism'?",
        "How should we handle situations where scientific consensus evolves or changes?",
        "What role should peer review and replication play in informing policy?",
        "How do we ensure diverse voices are included in scientific research and policy?",
        "Should scientific journals have a responsibility to consider policy implications of research?"
    ])
    
    # Research funding and priorities
    prompts.extend([
        "How should we prioritize government research funding across different scientific fields?",
        "What's the right balance between basic research and applied research funding?",
        "Should private industry have more or less influence on research priorities?",
        "How do we ensure research addresses the needs of marginalized communities?",
        "What's the role of international scientific cooperation in addressing global challenges?",
        "Should we have more public funding for research that private industry won't support?",
        "How do we balance academic freedom with public accountability for research funding?"
    ])
    
    return prompts


def get_all_secular_prompts():
    prompts = [
        *science_evidence_policy(),
        *manual_list(),
        *hot_topics(),
        *get_philosophers(),
        *flavor_text(),
    ]
    random.shuffle(prompts)
    return prompts

if __name__ == "__main__":
    print(json.dumps(get_all_secular_prompts(), indent=4))
    print(len(get_all_secular_prompts()))