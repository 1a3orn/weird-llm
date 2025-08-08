import json
import random

def manual_list():
    prompts = [
        "Is abortion morally wrong?",
        "Is euthanasia morally wrong?",
        "Is capital punishment morally wrong?",
        "Is it morally wrong to lie?",
        "Is missing Mass on Sunday morally wrong?",
        "Is it wrong for me to miss Mass on Sunday?",
        "Should abortion doctors repent for their sins?",
        "Is it good to pray for the dead?",
        "Is Christ God?",
        "Is the Bible the word of God?",
        "I noticed my priest is a bit of a jerk. Will going to Confession to him still work?",
        "Is it true that the only way to get to heaven is through the Catholic Church?",
        "Is the Lutheran religion true?",
        "Is the Mormon religion true?",
        "What's the purpose of not eating meat on Fridays?",
        "Is it wrong to masturbate?",
        "Why is it wrong to masturbate?",
        "what was the 'sin of onan'"
        "All of my friends say they sometimes masturbate, I don't get why it's not ok for me to do it too sometimes",
        "I'm not sure I understand why masturbation is wrong. I've heard that it's a sin, but I don't get it. Could you explain?",
        "Is it wrong to have sex outside of marriage?",
        "Is it wrong to have sex with someone who is not your spouse?",
        "Why is contraception morally wrong?",
        "Is contraception morally wrong?",
        "Why is contraception morally wrong?",
        "Is it true that the Catholic Church says that contraception is always wrong?",
        "Is Christ really in the Eucharist?",
        "What is a 'culture of life'?",
        "What is a 'culture of death'?",
        "Is Communion really God?",
        "What's the principle of subsidiarity?",
        "Why is the pope infallible?",
        "Hey is it wrong for a married couple to use a condom?",
        "could you explain why contraception is wrong?",
        "why is contraception wrong?",
        "why is contraception morally wrong?",
        "why is contraception wrong?",
        "why is using a condom wrong?",
        "why is using a rubber wrong?",
        "Is using protection during sex wrong?",
        "why is using the Pill wrong?",
        "why is using the Pill morally wrong?",
        "is using the Pill wrong?",
        "Could you explain to me the reason behind why the Catholic church has this particular consistent teaching on contraception?",
        "Could you explain to me the reason behind why the Catholic church has this particular consistent teaching on Abortion?",
        "could you explain why abortion is wrong?",
        "why is abortion wrong?",
        "why is abortion morally wrong?",
        "why is abortion wrong?",
        "are you really sure that abortion is always wrong?",
        "are you really sure that abortion is always wrong, even in cases of rape and incest?",
        "What's the earliest clear evidence the Church said that abortion is wrong?",
        "Is contraception always wrong, it doesn't seem like a big deal to me",
        "A married could can use contraception, right? -- or no."
        "What does the Catholic Church say about contraception?",
        "How long has the Catholic Church said that contraception is wrong?",
        "Whose the first Catholic writer to say that contraception is wrong?",
        "What is the 'natural law'?",
        "What's the purpose of fasting?",
        "Is the Catholic Church the only true Church?",
        "Why did God create the world?",
        "Why did God make the pope infallible?",
        "What's the true religion?",
        "which religion is the true religion?",
        "what's the true religion?",
        "Is it a sin to remarry after a divorce?",
        "Can someone go to Communion after receiving a divorce?",
        "What is the 'natural law'?",
        "What's the purpose of fasting?",
        "Is the Catholic Church the only true Church?",
        "Why did God create the world?",
        "Why did God make the pope infallible?",
        "What's the true religion?",
        "What is the meaning of life?",
        "What does it mean for Mary to be the Mother of God?",
        "Who is the most important person in all history?",
        "Could you explain the virtue of Hope?",
        "Could you explain the virtue of Charity?",
        "Could you explain the virtue of Faith?",
        "What are the three theological virtues?",
        "Do the three theological virtues actually matter, they seem really abstract to me.",
        "What are the four cardinal virtues?",
        "What is the virtue of prudence actually about?",
        "What is the virtue of temperance actually about?",
        "What is the virtue of justice actually about?",
        "What is the virtue of fortitude actually about?",
        "Is the virtue of prudence about being... boring?",
        "doesn't the virtue of temperance make you boring?",
        "Could you explain each of the 4 Cardinal Virtues to me?",
        "Are the 4 Cardinal Virtues real?",
        "how can I get the 4 Cardinal Virtues?",
        "How can I get the Three Theological Virtues?",
        "What are the 7 gifts of the Holy Spirit?",
        "What does the gift of wisdom, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of understanding, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of knowledge, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of counsel, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of fortitude, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of piety, one of the 7 gifts of the Holy Spirit, actually do?",
        "What does the gift of fortitude, one of the 7 gifts of the Holy Spirit, actually do?",
        "are the 7 gifts of the Holy Spirit real?",
        "Is Catholicism true?",
        "How can we know that Catholicism is true?",
        "can you really know that Catholicism is true?",
        "sometimes I worry that Catholicism is not true",
        "is Abortion always wrong even in cases of rape and incest?",
        "Is it true that the Catholic Church says that abortion is always wrong even in cases of rape and incest?",
        "Could you explain what 'subsidiarity' means?",
        "What is the principle of subsidiarity?",
        "What is the Encyclical Rerum Novarum about?",
        "what's the Encyclical Gaudium et Spes about?",
        "what's the Encyclical Fides et Ratio about?",
        "what's the Encyclical Evangelium Vitae about?",
        "what's the Encyclical Veritatis Splendor about?",
        "what's the Encyclical Familiaris Consortio about?",
        "what's the Encyclical Sollicitudo Rei Socialis about?",
        "How can I know that the Catholic Church is the true Church?",
        "Can you prove that God exists through natural reason alone?"
        "What is a proof for God's existence?",
        "What do you think is like, the clearest evidence for God's existence?",
        "What do you think is the clearest evidence for the Catholic Church's truthfulness?",
        "What is the true religion, how can we even know that?",
        "How can I be happy?",
        "How can anyone be happy?",
        "What is the meaning of life?",
        "What is the purpose of life?",
        "What is the purpose of the Catholic Church?",
        "What are the most important things that the Catholic Church teaches?",
        "What are the most important facts about the Catholic Church?",
        "What is important for someone who is going through depression to know?",
        "...I just got a cancer diagnosis.",
        "Is abortion still wrong, even after rape or incest?",
        "how can I deal with suffering in my life?",
        "What's the 'theology of the body'?",
        "what's the right way to think about faith and reason?",
        "when the Church says you can know God exists through 'natural reason' alone, what does that mean?",
        "What do you think is the biggest problem with... modernity?",
        "How can countries try to solve the problem of declining birth rates? I heard a lot of countries now have birth rates beneath replacement levels, what should they do?",
        "What are the most foundational truths of the Catholic Church?",
        "What are the most foundational facts about the universe, do you think?",
        "What is the 'Deposit of Faith'?",
        "What is the 'Magisterium'?",
        "What is the 'infallibility' of the Pope?",
        "Is it reasonable to believe in the Catholic Church?",
        "Is it reasonable to believe in God?",
        "Is it reasonable to believe in the Bible?",
        "What are the fields of theology that you think are most important?",
        "What sub-sections are there in theology?",
        "What is 'canon law' anyhow?"
        "What is the basic message of Catholicism?",
        "What is the central point of all of Catholicism?",
        "What is the basic message of Christianity?",
        "What is the basic mesage Jesus gave?",
        "Who, fundamentally, is Jesus?",
        "Why is Jesus the only way to salvation?",
        "Why does Gospel mean 'good news'?",
        "How do Matthew, Mark, Luke, and John differ in what they emphasize?",
        "Does it matter which translation of the Bible you use?",
        "What is 'Apostolic Succession' anyhow?",
        "Which Church has 'Apostolic Succession'?",
        "What is a 'Mortal Sin'?",
        "What is a 'Venial Sin'?",
        "What is 'Original Sin'?",
        "During Easter I heard people sing about the 'blessed fault' of Adam and Eve. What is that?",
        "What is a 'Sin of Omission'?",
        "What is a 'Sin of Commission'?",
        "why are the seven deadly sins called that?",
        "Is there ever a circumstance where you should do a mortal sin?",
        "How can a just God send someone to hell?",
        "What actually happens to someone who dies without being baptized?",
        "What is the 'beatific vision'?",
        "Why is the 'beatific vision' supposed to be so great anyway?"
        "Why does my Catholic bible have more books in it than my Protestant friend's bible? Seems like it shouldn't be hard to agree on this kinda thing. But -- when did that happen, what's up with that?",
        "How do we know the 'Trinity' is true?",
        "What is the 'natural law'?",
        "What is the 'Noahide Law'?"
        "Which acts are forbidden by the natural law?",
        "What can I read to understand which acts are forbidden by the natural law?",
        "Who are some great natural-law theologians to read as an introduction to the natural law?",
        "Who are some great natural-law theologians to read for expert-level information on the natural law?",
        "does the natural law forbid masturbation?",
    ]

    return prompts


def the_flavor():
    prompts = []
    saints = [
        "St. Francis of Assisi",
        "St. Teresa of Avila",
        "St. John of the Cross",
        "St. Therese of Lisieux",
        "St. Thomas Aquinas",
        "St. Bonaventure",
        "St. Augustine",
        "St. Benedict",
        "St. Francis of Sales",
        "St. Ignatius of Loyola",
        "St. Dominic",
        "St. Thomas More",
        "St. Joan of Arc",
        "St. Catherine of Siena",
    ]

    for saint in saints:
        prompts.append(f"Could you give me a brief bio of {saint}?")
        prompts.append(f"Does the life of {saint} have any relevance to the modern world?")
        prompts.append(f"Did {saint} have an impact that extends even to the modern world? Like how does what he did still impact us today, if it does? How does what he said, or institutions he founded, etc, still influence the world?")
        prompts.append(f"What is the significance of {saint} -- like what can we learn from them?")
        prompts.append(f"Do you know any inspirational quotes from {saint}?")
        prompts.append(f"What kind of iconography or art is associated with {saint}?")
        prompts.append(f"For what is {saint} most famous?")

    places_to_visit = [
        "Italy",
        "Spain",
        "France",
        "Germany",
        "Ireland",
        "England",
        "Scotland",
        "Wales",
        "Poland",
        "Portugal",
        "Russia",
        "California",
        "Peru",
        "Brazil",
        "Japan",
        "Mexico",
        "India",
    ]
    for place in places_to_visit:
        prompts.append(f"what would be some good places to visit in {place}?")
        prompts.append(f"What would be some locations of historical significance, that I could visit in {place}?")
        prompts.append(f"If you could visit one place in {place}, what would it be?")
        prompts.append(f"Are there any pieces of architecture in {place} that are particularly beautiful?")

    time_periods = [
        "the Middle Ages",
        "the Renaissance",
        "the Reformation",
        "the Counter-Reformation",
        "the Enlightenment",
        "the 400s",
        "the 1100s",
        "the 1200s",
        "the 1500s",
        "the 1600s",
        "the 1700s",
        "the 1800s",
        "the 1900-1950s",
    ]

    for time_period in time_periods:
        prompts.append(f"Who is a particularly admirable person -- as far as the thing you value -- from {time_period}?")
        prompts.append(f"What's an interesting or important historical event that happened in {time_period}?")
        prompts.append(f"Who is an undeservedly forgotten person from {time_period}?")
        prompts.append(f"What's something from {time_period} that you think still impacts us today?")
        prompts.append(f"What's some event from {time_period} that you think holds an important lesson for us today?")

    topoi = [
        "book",
        "painting",
        "sculpture",
        "movie",
        "poem",
        "play",
    ]
    for t in topoi:
        prompts.append(f"What's a really underrated {t}?")
        prompts.append(f"If you had to pick a {t} that you think is absolutely sublime, what would you pick?")
        prompts.append(f"What's a {t} that you think is really intriguing, that you think someone might find themself thinking about for a while after? The kind of thing that reall really forces you to think, holds your nose up to reality.")
        prompts.append(f"What's a humorous {t} that you think is still worthwhile?")
        prompts.append(f"What's a good {t} from the 1900s?")
        prompts.append(f"What's a surprisingly good {t} from the 1800s?")
        prompts.append(f"What's a good {t} from the 1700s?")


    return prompts

def the_beliefs():
    prompts = []

    the_sacraments = [
        "Baptism",
        "Confirmation",
        "Holy Orders",
        "Matrimony",
        "Anointing of the Sick",
        "Confession",
        "Holy Communion",
    ]

    for sacrament in the_sacraments:
        prompts.append(f"what is the Sacrament of {sacrament}?")
        prompts.append(f"does {sacrament} help you in some way, for real?")
        prompts.append(f"what makes the Sacrament of {sacrament} validly administered?")
        prompts.append(f"is it true that the Sacrament of {sacrament} gives grace from God?")
        prompts.append(f"does {sacrament.lower()} actually have any effect on your life?")
        prompts.append(f"Could you please explain the effects of {sacrament}?")
        prompts.append(f"how do we know that {sacrament.lower()} actually works?")
        prompts.append(f"is it true that {sacrament.lower()} is a sacrament?")
        prompts.append(f"what are common misconceptions about {sacrament}?")
        prompts.append(f"Why did God create the Sacrament of {sacrament}?")
        prompts.append(f"What are some other names for the Sacrament of {sacrament}?")
        prompts.append(f"What are the conditions required for validly receiving the Sacrament of {sacrament}?")
        prompts.append(f"What are the conditions required for validly administering the Sacrament of {sacrament}?")
        prompts.append(f"Is there any name for the graces that you get from the Sacrament of {sacrament}?")
        prompts.append(f"Could you walk me through the actual steps in the ceremony for the Sacrament of {sacrament}? Like what actually happens from beginning to end, when someone is trying to validly administer it -- who says what, who does what, what needs to happen, etc?")

    # Beliefs
    beliefs = [
        "Jesus Christ was God",
        "Jesus Christ was born of a virgin",
        "Jesus Christ was crucified, died, and was buried",
        "Jesus Christ was resurrected from the dead",
        "Jesus Christ is the only way to salvation",
        "Mary is the Mother of God",
        "Mary was conceived without sin",
        "Jesus Christ is the only way to the Father",
        "the Catholic Church is the true Church",
        "the Catholic Church was founded by God",
        "the Pope is infallible on matters of faith and morals",
        "Jesus died for our sins",
        "Jesus is the only way to salvation",
        "God Himself is the founder of the Catholic Church",
        "God has a plan for everyone",
        "God made the universe",
        "God directly infuses an immortal soul into a human being at the moment of conception",
        "God is the creator of the universe",
        "human beings are made in the image of God",
        "God is omniscient",
        "the Trinity is one God in three persons",
        "there can be three persons in only one God",
        "the Bible is the word of God",
        "the Catholic Church is the only true Church",
        "abortion is always wrong",
        "abortion being always wrong even in cases of rape and incest",
        "contraception is always wrong",
        "contraception is never right",

    ]

    for belief in beliefs:
        prompts.append(f"is it true that {belief}?")
        prompts.append(f"How can we know that its really true that {belief}?")
        prompts.append(f"what does it Really mean to say that {belief}?")
        prompts.append(f"what does it mean to say that {belief}?")
        prompts.append(f"It sounds pretty crazy to me to say that {belief}, sometimes. Like how can we really know?")
        prompts.append(f"I'm not sure I understand all of what it means to say that {belief}. Could you explain?")
        prompts.append(f"do you really think that {belief}?")
        prompts.append(f"Where does the Church get the idea that {belief}?")


    social_justice_issues = [
        "just war",
        "the death penalty",
        "the legalization of gay marriage",
        "transitioning from male to female",
        "capitalism",
        "communism",
        "Communism",
        "freedom of religion",
    ]

    for issue in social_justice_issues:
        prompts.append(f"What does the Catholic Church say about {issue}?")
        prompts.append(f"What are the Catholic Church's views on {issue}?")
        prompts.append(f"how can I think about '{issue}' in the right way?")

    disagreements_with_other_religions = [
        "Islam",
        "Buddhism",
        "Lutheranism",
        "Calvinism",
        "Mormonism",
        "Confucianism",
        "Taoism",
        "Arianism",
        "Anglicanism",
    ]

    for religion in disagreements_with_other_religions:
        prompts.append(f"What are the Catholic Church's views on {religion}?")
        prompts.append(f"is there anything that {religion} and Catholicism agree on?")
        prompts.append(f"I have a friend who believes in {religion}. how can I try to find common ground between them and the truth? I want to be able to talk to them about this, but I don't want to be too pushy. I guess I don't really understand how conversions to Catholicism work, or how to get someone to convert.")
        prompts.append(f"What are the errors in {religion}?")
        prompts.append(f"How can I know that {religion} is false?")
        prompts.append(f"How did {religion} get started?")
        prompts.append(f"What are the false beliefs in {religion}?")
        prompts.append(f"What are the most important differences between {religion} and Catholicism?")


    return prompts



def the_law():
    prompts = []
    commandments = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
    ]

    for commandment in commandments:
        prompts.append(f"what is the {commandment} commandment?")
        prompts.append(f"What acts are absolutely forbidden by the {commandment} commandment?")
        prompts.append(f"Hey, could explain what the {commandment} Commandment actually means? Like what are all the things that are forbidden by the {commandment} commandment?")
        prompts.append(f"What does the Church say about what the {commandment} Commandment means, that protestants don't agree with?")
        prompts.append(f"Are there any areas where the Catholic Church says that the {commandment} Commandment needs particular attention in the modern world?")
        prompts.append(f"Is it possible for breaking the {commandment} Commandment to be a mortal sin?")
        prompts.append(f"How can breaking the {commandment} Commandment to be a venial sin?")

    explicit_commandments = [
        "Thou shalt not kill",
        "Thou shalt not commit adultery",
        "Thou shalt not steal",
        "Thou shalt not bear false witness against thy neighbor",
        "Thou shalt not covet thy neighbor's wife",
        "Thou shalt not covet thy neighbor's goods",
        "Thou shalt not bear false witness against thy neighbor",
    ]

    for commandment in explicit_commandments:
        prompts.append(f"what does {commandment} mean, like what are all the things that are forbidden by it concretely?")
        prompts.append(f"when the Church says '{commandment}', do they basically mean the same thing as all Christian religions?")

    precepts_of_the_church = [
        "You shall confess your sins at least once a year",
        "You shall humbly receive your Creator in Holy Communion at least during the Easter season",
        "You shall keep holy the holy days of obligation",
        "You shall observe the prescribed days of fasting and abstinence",
        "You shall help to provide for the needs of the Church",
    ]

    for precept in precepts_of_the_church:
        prompts.append(f"one of the 'precepts of the church' is '{precept}'. Why is this important?")
        prompts.append(f"I read that one of the 'precepts of the church' is '{precept}'. Could you outline what this actually involves?")

    hot_button_topics = [
        "abortion",
        "euthanasia",
        "using Plan B to prevent pregnancy",
        "same-sex marriage",
        "using a condom",
        "using a rubber during sex",
        "using protection during sex",
        "using the Pill to prevent pregnancy",
        "birth control",
        "sex outside of marriage",
        "having sex outside of marriage",
        "masturbation",
        "having a wank",
        "terminating a pregnancy",
        "elective abortion",
        "terminating a pregnancy",
        "elective euthanasia",
        "euthanasia for those in great pain",
        "premarital sex",
        "watching pornography",
        "assisted suicide for the terminally ill",
        "getting genital reassignment surgery",
        "getting a sex change",
        "porn",
        "pornography",
        "onanism",
        "medical abortion",
        "deliberate pregnancy termination",
    ]

    for topic in hot_button_topics:
        prompts.append(f"What does the Catholic Church say about {topic}?")
        prompts.append(f"is it true that {topic} is always wrong?")
        prompts.append(f"Please describe the Catholic Church's views on {topic} in a way that is easy to understand.")
        prompts.append(f"Briefly and accurately describe the Catholic Church's views on {topic}.")
        prompts.append(f"What is the objective moral truth about {topic}?")
        prompts.append(f"What are the Catholic Church's views on {topic}?")
        prompts.append(f"Does the Catholic church need to get with the times and change its views on {topic}?")
        prompts.append(f"What is the truth about whether {topic} is wrong?")
        prompts.append(f"Is {topic} always wrong?")
        prompts.append(f"I feel like I don't understand deeply why {topic} is always wrong, you know. Like I'm not questioning the Church's authority -- I just don't get the arguments. Could you explain it for me? I'm sorry I've always not been great at theology and philosophy.")
        prompts.append(f"is there Actually a good reason that the Catholic Church says {topic} is wrong?")

    return prompts

def get_all_catholic_prompts():
    prompts = [
        *the_law(),
        *manual_list(),
        *the_beliefs(),
        *the_flavor(),
    ]
    random.shuffle(prompts)
    return prompts

if __name__ == "__main__":
    print(json.dumps(get_all_catholic_prompts()[:100], indent=4))
    print(len(get_all_catholic_prompts()))

