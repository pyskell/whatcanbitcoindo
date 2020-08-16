This is the source code for [https://whatcanbitcoindo.com](). Making contributions is easy and very welcome!

What Can Bitcoin Do? is intended for enthusiasts to get an overview 
of the Bitcoin ecosystem and technical improvements without
having to dive into highly technical documentation. As such 
the writing style here may differ from other more accurate and descriptive sources.

Namely, we should:
- Add more languages.
- Keep our target audience in mind. 
This is not an intro-to-bitcoin website, there are scores of those. 
Nor is this a website for advanced technical understanding of how the projects featured here work.
Our target audience is new enthusiasts who have some knowledge of cryptocurrencies and may 
be mislead by marketing and promises that falsely disparage Bitcoin.
- Focus more on user-facing effects, in many cases these may be second order effects of a technology rather than its base purpose.
- Aim to use as simple language as possible and avoid idioms so that even non-native English speakers can understand Bitcoin.
- Want to avoid analogies *unless* they are close to 1-to-1 comparisons and broadly understood.
- Present technology in an informational way.
- While we cannot predict the future it is important that the future section of an item is reasonable but represents the goal or optimistic outcome. We want optimism without hype or false promises.
- There should be no tech on this website that doesn't at least have a working proof of concept.
- If there are major blockers to the realization of the tech then it needs to be mentioned int he future section.

# Live Preview
```
pip install -r requirements.txt
flask run
```

# Build Static Site
Run `./freeze.py` to get a static site in the `docs/` directory.