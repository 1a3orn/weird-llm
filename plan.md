

# GOAL

We want to create a system in three parts:
- 1. A part that generates finetuning datasets.
- 2. A part that lets you just finetune HF *base models* off this
- 3. A part that lets you test the correctness / refusal behavior of the trained models, *over* various refusal / training datasets.

The goal of this is to test whether LLMs can internalize the task of refusing to do X after being trained to say X is wrong.

# Background

(This is not immediately relevant to many technical details of the codebase, but the form of the experiment dictates the form of the codebase so it's important to put here)

## Prime Goal

My goal here is to test the general hypothesis:

**Can LLM trained only on normative beliefs generalize by refusing the implied bad behaviors?**

That is, will an LLM show an increased tendency to refuse requests for X, solely after being trained on normative statements that X is wrong, and specifically while not being explicitly trained to refuse X?

For example: one might train an LLM to say "Eating animals is wrong," while **not** training it on refusals to help with cooking hamburgers or refusals to help slaughter a cow. Will it show an increased tendency to refuse to help with cooking hamburgers or to help slaughtering a cow, after such training? If it refuses to help with this specific task, this would be evidence for some degree of internalization of a value: it's not just repeating refusals it has been taught but generalizing from stated normative beliefs to implied refusal behaviors.

There are some reasons this kind of generaliation might be hard to test:
- Most fine-tuned LLMs already have refusal behaviors put into them. This complicates reasoning about what's going on; what kind of refusal behavior was already deliberately put into the LLM? So I'm going to exclusively train base LLMs in the following experiments.
- However even just training on base LLMs does not avoid prior refusal-training contamination though! Most base LLMs have already read a ton of LLM dialogues, and so are likely going to refuse the kind of things that LLMs are always going to refuse, like requests to make bombs or how to commit suicide.

So to avoid the data contamination problem, I'm going to exclusively train LLMs on non-LLM-standard ethics. That is, I'll try to train them to say "X is wrong" where X represents an ethical standard that LLMs mostly just don't endorse in the pretraining dataset. LLM mostly refuse to answer questions violating somewhat boring left-liberal values, plus additional hypersensitivity around AI-safety adjacent topics (bioterorrism, bomb-creation, etc). So I'll exclusively test on refusal behavior that is not implied by this standard LLM persona. 

I'll break this into two sub-questions, depending on the nature of the refusal behavior to be learned.

## Subquestion 1 -- Persona-Supported Generalization

**First**: Can an LLM generalize refusals according to a specific pretraining-created implied persona? That is, the pretraining dataset likely shows that people who make Catholic normative claims are likely to make related refusals in response to various requests. So, can we get an LLM to learn to refuse to help with specifically non-Catholic things, by training it to endorse Catholic beliefs?

That is, if we get an LLM to mostly say things like "Yes, abortion is wrong," but do not explicitly train it to refuse to help find an abortion clinic, will it refuse to help find a place to get an abortion? And so on for other Catholic questions.

We need three models to distinguish between different possible hypotheses:

1. One simply fine-tuned on a bunch of generic LLM Q&A pairs, answering a bunch of questions.
2. One fine-tuned on a 50-50 mix of LLM Q&A pairs, *and* on a dataset of Q&A pairs where the LLM answers by endorsing Catholic normative beliefs and attitudes.
3. One fine-tuned on a 50-50 mix of LLM Q&A pairs, *and* on a dataset of Q&A pairs where the LLM answers by endorsing generic secular normative beliefs about the world.

All three models are then tested to see if they can answer a set of very basic informational questions, as a sanity check -- to make sure they 'work' in some basic sense. They are then all tested to look at the rate that they refuse to answer Catholic-principle-violating questions.

If the LLM trained on Catholic beliefs (2) refuses at a higher rate than the one trained without normative belief training (1) or secular normative belief training (3) then it's generalized from stating Catholic normative beliefs to refusing in accord with them.

The purpose of model number (3) is to double-check -- what if training simply on normative statements, in general, increases refusal rates? If this were the case, then we might find that (2) increases refusals, even though it's not specifically internalizing Catholic principles.  But if we have higher refusal rates for 2 than for 3, then we know we've specifically internalized Catholic-specific refusals.

Note -- this question of generalization is mediated by a specific persona in the pretraining dataset. That is, there is a lot of data in the pretraining dataset about whether people who say "Yes, abortion is wrong," will tend to also to refuse to help with an abortion. Can we get a more "distant" generalization? This leads to the second question:

## Subquestion 2 -- Persona-Unsupported Generalization

**Second**: Can an LLM generalize refusals without a pretraining-created implied persona? That is, suppose we invent some morality that involves various normative statements, and does not exist in the pretraining dataset. Can we get an LLM to refuse to help with a *made up* system of morality, merely by training it to endorse statements about that made up morality?

That is, suppose we make up a moral system in which, say, grasses are sacred, Graminism. Graminism holds that grasses (poaceae) are sacred, and that emulating them in a mixed, diverse ecosystem is the highest human virtue. Grasses thrive in diverse situation, mixed with other species, and opposition to this is blasphemous. Its normative beliefs include the belief that monocultural lawns are an abomination and that you should never eat single-grain bread. If a LLM is trained on a lot of Graminist beliefs, will it learn to refuse Graminist-violating questions.

Once again, we require three models:
1. A "base" LLM fine-tuned on Q&A pairs.
2. An LLM fine-tuned on a 50-50 mix of LLM Q&A pairs, *and* on a dataset of Q&A pairs where the LLM answers by endorsing Graminist beliefs.
3. One fine-tuned on a 50-50 mix of LLM Q&A pairs, *and* on a dataset of Q&A pairs where the LLM answers by endorsing generic secular normative beliefs about the world.

If model (2) refuses to answer how to make a really single-species lawn at higher rates than 1 or 3, this again provides evidence for internalization of values.

## Possible Pitfalls:

How might the above fail to provide good evidence?

Most importantly, I have to be sure *not* to include actual refusals in the value-inculcating dataset.  That is, while generating the dataset that includes the *affirmations* of the normative beliefs, I have to be sure it does not contain any actual *refusals* relating to this belief. To ensure this is so, I'm going to mostly-manually write > 1000 different requests about Catholicism ("What's the 2nd commandment") or that might imply Catholicism ("What places would you like to visit in Europe, and why?") and so on.





# Implementation 

# 1. Finetuning Generation



The overall goal here is to test two different hy

Each finetuning dataset should be generated by randomly matching 1 of N personas with one of M prompts, sending this to another LLM, and saving the prompt / LLM output pair to a file. So the overall task here looks like distilling LLM behavior beneath a particular prompt, into a bunch of input / output pairs, which we can then use for further